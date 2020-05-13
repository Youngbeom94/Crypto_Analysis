#-------------------------
# 암호분석 2020
#-------------------------

import TC20_Enc_lib, TC20_Dec_lib
import pickle    # 변수 저장
import random    # 난수 생성
import copy      # 딥 카피 (깊은 복사) 


#--- TC20 with 24 bit key
#  Key = [0,*,*,*] --
#                    |
#    PT = [*,*,*,*] --> CT = [*,*,*,*] 

#--- 키 크기, TMTO 테이블 크기  (키크기 = 행크기 x 열크기)
key_bit = 24        # key = [0,*,*,*]

#============================================================
# 이전에 만든 함수들
#============================================================
#--- int(4bytes) to list 0x12345678 -> [ 0x12, 0x34, 0x56, 0x78 ]
def int2list(n):
    out_list = []
    out_list.append( (n >> 24) & 0xff )
    out_list.append( (n >> 16) & 0xff )
    out_list.append( (n >>  8) & 0xff )
    out_list.append( (n      ) & 0xff )

    return out_list

#--- list to int [ 0x12, 0x34, 0x56, 0x78 ] -> 0x12345678
def list2int(l):
    n = 0
    num_byte = len(l)
    for i in range(len(l)):
        n += l[i] << 8*(num_byte - i -1)
        
    return n

#- 변수를 파일에 저장하기
def save_var_to_file(var, filename):
    f = open(filename, 'w+b')
    pickle.dump(var, f)
    f.close()
    
#- 파일에서 변수를 가져오기
def load_var_from_file(filename):
    f = open(filename, 'rb')
    var = pickle.load(f)
    f.close()
    return var
#============================================================


#============================================================
# X_{j+1} = E(P0, X_{j})  # key bit = block size
# X_{j+1} = R( E(P0, X_{j}) )  # R: 32비트 -> 24비트
# SP = X0(Key) -> X1 -> X2 -> ... -> Xt = EP  (encryption chain)
#============================================================

#---------------------
# R: 32비트 -> 24비트
# 암호문 [a,b,c,d] --> 암호키 [0,b,c,d]   
def R(ct):
    # next_key = ct (ct의 내용이 함께 바뀐다)
    next_key = copy.deepcopy(ct)
    next_key[0] = 0
    return next_key

#---------------------
# Encryption chain 만들기
# 입력:    
#   시작점: SP(24비트 랜덤키)
#   고정평문: P0 (32비트)
#   길이: t (체인의 길이 t=2^8 = (2^24)^(1/3))
# 출력:
#   끝점: EP    
def chain_EP(SP, P0, t):
    Xj = SP
    for j in range(0,t):
        ct = TC20_Enc_lib.TC20_Enc(P0, Xj)
        Xj = R(ct)  # X_{j+1}
    return Xj

def chain_EP_print(SP, P0, t):
    Xj = SP
    print('SP =', SP)
    for j in range(0,t):
        ct = TC20_Enc_lib.TC20_Enc(P0, Xj)
        Xj = R(ct)  # X_{j+1}
        print('-->', ct, ' -->', Xj)
    return Xj

def chain_EP_file(SP, P0, t, chain_num, table_num):
    file_name = 'debug/TMTO-chain-' + str(table_num) +'-' + str(chain_num) + '.txt'
    f = open(file_name, 'w+')
    Xj = SP
    #print('SP =', SP)
    f.write('SP = [0, %d, %d, %d] \n' %(Xj[1], Xj[2], Xj[3]))
    for j in range(0,t):
        ct = TC20_Enc_lib.TC20_Enc(P0, Xj)
        Xj = R(ct)  # X_{j+1}
        #print('-->', ct, ' -->', Xj)
        f.write(' --> [%d, %d, %d, %d] ' %(ct[0], ct[1], ct[2], ct[3]))
        f.write(' --> [%d, %d, %d, %d] \n' %(Xj[0], Xj[1], Xj[2], Xj[3]))
    f.close()
    return Xj

#---------------------
# TMTO 테이블 한개 만들기
# 입력:
#   P0: 고정평문 
#   m: 행(row)의 개수 (체인의 개수)
#   t: 열(col)의 개수 (체인의 길이)
#   ell: 테이블 번호 (TMTO 테이블 번호: 0,1,2, ..., 255)
def make_one_tmto_table(P0, m, t, ell):
    tmto_dic ={}  # = {(SP0, EP0), (SP1, EP1), ... , (SP_{m-1}, EP_{m-1}) }
    for i in range(0,m):
        SP = [0, random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        EP = chain_EP_file(SP, P0, t, i, ell)
        SP_int = list2int(SP)
        EP_int = list2int(EP)
        tmto_dic[EP_int] = SP_int
    file_name = 'debug/TMTO-' + str(ell) + '.dic'
    save_var_to_file(tmto_dic, file_name)
        
#---------------------
# TMTO 테이블 전체 만들기
# 입력:
#   P0: 고정평문 
#   m: 행(row)의 개수 (체인의 개수)
#   t: 열(col)의 개수 (체인의 길이)
#   num_of_tables: TMTO 테이블 개수 (=256)    
def make_all_tmto_tables(P0, m, t, num_of_tables):
    print('makeing TMTO tables', end='')    
    for ell in range(0, num_of_tables):
        make_one_tmto_table(P0, m, t, ell)
        print('.', end='')
    print('\n %d TMTO tables are created.\n' %(num_of_tables))


#------------------
#  한개의 테이블을 읽고 후보 암호키를 리스트에 넣는다.
# 입력:
#    ct = E(P0, unknown_key)    
#   m: 행(row)의 개수 (체인의 개수)
#   t: 열(col)의 개수 (체인의 길이)
#   ell: 테이블 번호 (TMTO 테이블 번호: 0,1,2, ..., 255)  
def one_tmto_table_search(ct, P0, m, t, ell):
    key_candid_list = []
    file_name = 'debug/TMTO-' + str(ell) + '.dic'
    tmto_dic = load_var_from_file(file_name)
    
    Xj = R(ct)
    current_j = t
    for idx in range(0,t):
        Xj_int = list2int(Xj)
        
        if Xj_int in tmto_dic:  # Xj가 EP 중에 있는지?
            SP = int2list(tmto_dic[Xj_int])  # EP --> SP
            key_guess = chain_EP(SP, P0, current_j-1)
            key_candid_list.append(key_guess)
            
        new_ct = TC20_Enc_lib.TC20_Enc(P0, Xj) 
        Xj = R(new_ct)
        current_j = current_j - 1
    
    return key_candid_list

#=====================================================
# (0) 실행
#=====================================================

random.seed(1234)  # 고정된 seed 사용 (고정되지 않은 seed 사용법은?)

P0 = [1,2,3,4]

m = 256 # 행(row)의 개수 (체인의 개수)
t = 256 # 열(col)의 개수 (체인의 길이)
tables = 256 # 테이블 개수

#=====================================================
# (1) TMTO 테이블 만들기
#=====================================================
'''
make_all_tmto_tables(P0, m, t, tables)
'''
#=====================================================
# (2) TMTO 공격 알고리즘
#=====================================================
ct1= [100, 107, 220, 57]


key_pool = []

print('TMTO Attack', end='')
for ell in range(0, tables):
    key_list = one_tmto_table_search(ct1, P0, m, t, ell)
    key_pool += key_list
    print('.',end='')

print('\n Attack complete!\n')
print(key_pool)

pt2 = [5,6,7,8]
ct2 = [72, 215, 32, 51]
final_key = []

for key in key_pool:
    ct_result = TC20_Enc_lib.TC20_Enc(pt2, key)
    if ct_result == ct2 :
        final_key.append(key)

print('Final key = ', end='')
print(final_key)

print(TC20_Enc_lib.TC20_Enc(P0, [0, 20, 90, 139])) #[100, 107, 220, 57]
print(TC20_Enc_lib.TC20_Enc(pt2, [0, 20, 90, 139])) #[72, 215, 32, 51]


