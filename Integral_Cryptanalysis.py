#-------------------------
# 암호분석 2020
#-------------------------

import ourAES_lib as AES   # 수업시간에 만든 AES 암호 라이브러리
import random              # 랜덤, 셔플링 함수
import copy                # 깊은복사(deepcopy)

#-----
# AES용 입력 평문 256개 만들기: (4x4 state) 256개
# 예: (Active, constant, constant, ... , constant)
#    [ [A,c,c,c], [c,c,c,c], [c,c,c,c], [c,c,c,c] ]
def plain_256(col, row):
    s256 = []
    new_state = []
    for i in range(4):
        # new_col = [ random.randint(0,255) for j in range(4) ]
        new_col = [ 1 for j in range(4) ]
        new_state.append(new_col)    
    for n in range(256):      
        new_state[3][0] = 255 - n  # 특정 바이트를 Active에 만든다.
        new_state[1][1] = n  # 특정 바이트를 Active에 만든다.
        # new_state[col][row] = n  # 특정 바이트를 Active에 만든다.
        s256.append(copy.deepcopy(new_state))  # 아래는 반드시 deepcopy로        
    return s256

#-----
# (4x4 state) 256개의 특정 위치(col, row)의 XOR 값 1바이트를 출력
# s256 = [ S0, S1, S2, ..., S255 ], 
#   Si = [ [Si[0][0], Si[1][0], Si[2][0], Si[3][0]], ... , [Si[0][3], Si[1][3], Si[2][3], Si[3][3]] ]
# 예: xor_256_pos(1,2,s256) = S0[2][1] xor S1[2][1] xor ... xor S255[2][1] 
def xor_256_pos(col, row, s256):
    xor_ed = 0
    for n in range(256):
        xor_ed ^= s256[n][col][row]
    return xor_ed

#-----
# (4x4 state) 256개의 XOR 값 16바이트를 출력
def xor_256(s256):
    xor_state = []
    for col in range(4):
        xor_col = [ xor_256_pos(col, row, s256) for row in range(4) ]
        xor_state.append(xor_col)
    return xor_state

#-----
# 256개 데이터로 구성된 리스트의 처음과 끝부분을 간략히 출력
def print_256_simple(x256, low=3, upper=253):
    #low = 3  #앞부분 출력위치
    #upper = 252 #뒷부분 출력위치
    for i in range(low):
        print('%3d: ' %(i), end= '') 
        print(x256[i])
    print('    ... ...')
    for i in range(upper,256):
        print('%3d: ' %(i), end= '') 
        print(x256[i])
    print('\n')
        
#-----
# 바이트로 구성된 리스트 출력
def print_byte_list(list, low=3, upper=253, line=16):
    for i in range(len(list)):
        if i < low:
            if (i%line)!=15:
                print(list[i], ' ', end='')
            else:
                print(list[i])
    for i in range(low, len(list)):
        if (i%line)!=15:
            print(list[i], ' ', end='')
        else:
            print(list[i])
    
#-----
# 길이 256의 랜덤 바이트열 만들기
# [0,1,2, ...,255] --> [252, 2, 15, ..., 7]   (랜덤 셔플링)
def byte256():
    list = [ i for i in range(256)] 
    random.shuffle(list)
    return list     


#===========================================
# 특성 확인용 함수
    
#-- (Active xor Active)
def ActiveActive():
    #Active 특성의 바이트열 2개 만들기
    Active1 = byte256()
    Active2 = byte256()
    
    Xor_A1_A2 = [ Active1[i]^Active2[i] for i in range(256) ]
    
    print('============================')
    print('=== (Active xor Active) ====\n')
    print('=== (Active byte 1) ===')
    print_256_simple(Active1)
    print('=== (Active byte 2) ===')
    print_256_simple(Active2)
    print('=== (output XOR) ===')
    print_256_simple(Xor_A1_A2)
    
    xor256 = 0
    for i in range(256):
        xor256 ^= Xor_A1_A2[i]
    print('===> XOR of 256 output =', xor256)
    print('============================\n')
    # 왜 XOR 결과가 0으로 나오는지 논리적으로 생각해보기!!!

#-- (Active * 0x02)  in  GF(2^8)
def Active_m02():
    print('==================================')
    print('=== (Active) x 0x02 in GF(2^8) ===\n')
    Active = byte256()
    m02_256 = [ AES.m02(Active[i]) for i in range(256) ]
    
    # 입력 Active 바이트
    print('== (Active byte) ==')
    print_byte_list(Active)
    print('== (Active) x 0x02 ==')
    print_byte_list(m02_256)
    
    sorted_m02_256 = m02_256.sort()
    print('== (Active) x 0x02 == (SORTED)')
    print_byte_list(m02_256)
    print('\n ==> (Active) x 0x02 = Active')
    print('==================================\n')
#===========================================
    
    
#-----
# 입력 Lambda-Set (256개 평문)
#       (Active, constant, constant, ... , constant)
# 입력이 각 라운드를 거치면서 Balanced 특성이 언제까지 유지되는지 확인
# 라운드: 1 라운드 ~ round 라운드
# => 실행해보면 3라운드 출력까지는 모든 바이트가 Balanced임을 알 수 있다.
def square_distinguisher(round):
    print('============================')
    print('== square_distinguisher() ==\n')
    
    #(1) 암호키는 임의로 선택
    key = [i for i in range(16)]  
    state_key = AES.block2state(key)
    
    #(2) 입력 평문 만들기 & 출력하기
    pt256 = plain_256(0,0)
    print('===(256 plaintexts)===')
    print_256_simple(pt256)

    #(3) 각 라운드 출력에 대하여 Balanced 특성을 살펴봄
    for i in range(1, round+1):
        ct256 = []
        #(3-1) i 라운드 암호화한 256개 데이터 만들기
        for n in range(256):
            ct = AES.AES_EncR(pt256[n], state_key, i) # i 라운드 암호화
            ct256.append(ct)
        #(3-2) 암호문 출력하기
        print('=== (%d round output)===' %(i))
        print_256_simple(ct256)
        #(3-3) 각 바이트를 XOR한 결과 출력하기(XOR결과가 0인 바이트는 Balanced 임)
        xor256 = xor_256(ct256)
        print('=== (output XOR)===')
        AES.hex_print(xor256)
        print('============================')
        print('\n')
        

#----
# Target Cipher: AES4() = AES 4 round   
# 입력평문(선택평문)에 대한 4라운드 AES 암호화 함수 AES4로 암호화한
# 암호문을 리턴한다. 
# (이 함수를 호출하는 공격자는 암호키는 모르고 암호화 함수만 사용한다)        
def AES4(pt_state):        
    # 설정된 암호키 (공격자가 모르는)
    key = [i for i in range(16) ]
    key_state = AES.block2state(key)
    # 라운드키 생성
    #rkey = AES.key_schedule_Enc(key_state)    
    #for round in range(5):
    #    print('round key %d =' %(round), end='')
    #    print(rkey[round])
    
    # 4라운드 암호화
    ct = AES.AES_EncR(pt_state, key_state, 4)
    return ct

#-----
# Integral Cryptanalysis of AES4 (4 round AES)
def IC_AES4(col=0, row=0):
    print('====================================')
    print('== Integral Cryptanalysis of AES4 ==')
    
    
    
    # 선택평문 256개 준비하기
    # (col, row) - 라운드키를 구할 위치
    #col = 4
    #row = 0
    pt256 = plain_256(col,row)
    # 암호문 저장하기
    ct256 = []
    for n in range(256):
        ct = AES4(pt256[n])
        ct256.append(ct)
    # 4라운드 키 한바이트 예측 - (col, row) 위치 예측
    key_list = []
    for key_guess in range(256):
        balanced256 = [ AES.ISbox[ct256[i][col][row]^key_guess] \
                       for i in range(256)]
        xored = 0
        for i in range(256):
            xored ^= balanced256[i]
        if xored == 0:
            key_list.append(key_guess)
    
    print('round key [%d][%d] = ' %(col, row), end='')
    print(key_list)
    print('====================================\n')     
        

#===========================================
# 예제 프로그램 실행


#==========================
#(1) Active, Balanced 특성 확인
# (Active xor Active)
# ActiveActive()

# (Active) x 0x02 in GF(2^8)
# Active_m02()


#==========================
#(2) 랜덤함수와 AES의 부분 라운드 암호화가 구별되는지 확인하는 함수 
square_distinguisher(3)


#==========================
# #(3) Integral Cryptanalysis 공격 예제

# #(3-1) 암호키 출력(공격자가 모르는 정보)   
# key = [i for i in range(16) ]
# key_state = AES.block2state(key)
# # 라운드키 생성
# rkey = AES.key_schedule_Enc(key_state)    
# for round in range(5):
#     print('round key %d =' %(round), end='')
#     print(rkey[round])
# print('\n')

# #(3-2) Integral Cryptanalysis 공격 구현
# # 선택평문 공격을 반복할때 공통으로 나오는 키 후보가 올바른 키로 판정한다 
# IC_AES4(0,0) # 구하는 4라운드 키 한바이트 위치 (col, row) 
# IC_AES4(0,0)
# IC_AES4(0,0)
# #=== [71] : 정답 키

# # 선택평문 공격을 반복할때 공통으로 나오는 키 후보가 올바른 키로 판정한다 
# IC_AES4(3,3)
# IC_AES4(3,3)
# IC_AES4(3,3)
# #=== [253] : 정답 키

