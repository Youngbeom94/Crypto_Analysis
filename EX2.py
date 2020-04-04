# -------------------------------
# 암호분석 2020.04.04, 20175204김영범
# HW2
# -------------------------------

import EX1
import random
'''
    Ex2.py
    암호키를 랜덤하게 생성하는 함수를 작성하고, 이를 이용하여 암호화 복호화하는 예제를 제시해라    
'''

def Key_generation():
    temp = list()
    for i in Alphabet:
        temp.append(i)
    random.shuffle(temp)
    usrkey = ''
    for j in temp:
        usrkey += j
    return usrkey


#---------------선 언------------------------
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ''
plaintxt = "hello world!"
ciphertxt = ''
recovered_msg = ''

def main():
#---------------Encrypt and Decrypt-----------
    key = Key_generation()
    EX1.Key_Validation(key)
    ciphertxt = EX1.Substitution_En(key,plaintxt)
    recovered_msg = EX1.Substitution_De(key,ciphertxt)
#---------------Print msg-----------
    print("key           = ", key)
    print("red_plain_txt = " , plaintxt)
    print("cipher_txt    = " , ciphertxt)
    print("recovetxt     = " , recovered_msg)

if __name__ == '__main__': 
    main()
