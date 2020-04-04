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

def Key_generation():#알파벳 26개를 이용해서 키를 랜덤으로 만들어주는 함수입니다.
    temp = list() # random함수는 문자열에서 사용이 불가능 하니까 list를 이용하려고 변수를 넣었습니다.
    for i in Alphabet:# temp list에 알파벳을 하나씩 추가시킵니다.
        temp.append(i)
    random.shuffle(temp) #random.suffle함수를 이용해서 temp list에 있는 26개를 무작위로 섞어줍니다.
    usrkey = ''
    for j in temp:#usrkey를 선언하고 무작위로 섞인 값들을 대입시켜줍니다.
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
