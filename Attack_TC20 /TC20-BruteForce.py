#-------------------------
# 암호분석 2020 20175204김영범
#-------------------------

import TC20_Dec_lib, TC20_Enc_lib
'''
정답 
given_pt = [0, 1, 2, 3]
key = [0,1,1,4]
given_ct = [187,225,23,152]

given_ct = [item for item in TC20_Enc_lib.TC20_Enc(given_pt, key)]
Cipher_message = [chr(num) for num in given_ct]

print('input plaintext =', given_pt)
print('output ciphertext =', given_ct)
print('Cipher_message =', Cipher_message)
'''

#==========================================================
#정수-> 리스트로
# ex) 0x12345678 - > [0x12,0x34,0x56...] 0
def int2list(n):
    out_list = []
    out_list.append(n>>24)
    out_list.append((n>>16) & 0xff)
    out_list.append((n>>8) & 0xff)
    out_list.append(n & 0xff)
    return out_list


#==========================================================
#리스트-> 정수
def list2int(lst):
    n = 0
    num_bytes = len(lst)
    for i in range(num_bytes):
        n += lst[i] << 8*(num_bytes - 1 - i)
        # i = 0: <<8*(4-1-0) = <<24
        # i = 1: <<8*(4-2-0) = <<16
    return n


##==========================================================
# lst = int2list(1<<16)
# n = list2int(lst)
# print(lst)
# print(n)

#==========================================================
given_pt = [0, 1, 2, 3]
given_ct = [192,126,66,83]

keysize = 1<<32 #key 20비트만 전수조사(최대:32비트)

print("Key searching", end = '')
for idx in range(0,keysize):
    guess_key = int2list(idx)
    pt = TC20_Dec_lib.TC20_Dec(given_ct,guess_key)
    if(pt == given_pt):
        print("\nkey = ", guess_key)
        # break
    if(idx % (1<<15)) == 0:
        print('.',end='')
#모든 키 후보를 리스트에 담아보기
#Np documentation available
