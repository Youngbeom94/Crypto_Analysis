# -------------------------------
# 암호분석 2020.04.04, 20175204김영범
# -------------------------------

import random
import os,sys

def ReadFile(in_file):
    if not os.path.exists(in_file):
        print('File %s does not exist' %(in_file))
        sys.exit()
    Infileobj = open(in_file)
    mytext = Infileobj.read()
    return mytext



def WriteFile(filename,msg):
    outfileobj = open(filename,'w')
    outfileobj.write(msg)
    outfileobj.close()
    return

def Substitution_En(key,msg):
    result = ''
    InSet = Alphabet
    Outset = key
    for char in msg:
        if char.upper() in InSet:
            idx = Alphabet.find(char.upper())
            if char.isupper():
                result += Outset[idx].upper()
            else:
                result += Outset[idx].lower()   
        else:
            result += char
    return result

def Substitution_De(key,msg):
    result = ''
    InSet = Alphabet
    Outset = key
    for char in msg:
        if char.upper() in Outset:
            idx = key.find(char.upper())
            if char.isupper():
                result += InSet[idx].upper()
            else:
                result += InSet[idx].lower()   
        else:
            result += char
    return result

def Key_Validation(key):
    check_alpha_number = list() #먼저 알파벳의 숫자를 파악하기 위한 0으로 초기화된 26개의 배열을 만듭니다.
    for i in range(len(Alphabet)):
	    check_alpha_number.append(0)# 0으로 초기화
    for char in key:#key안에 들어있는 알파벳을 하나씩 검사하고 순서를 이용해서 위에 선언한 배열에 1을 더해줍니다. 
        alpha_idx = Alphabet.find(char.upper()) #(ex. b가 key에 있었다면 chek_alpha_number[2]번째 값에 1을 더해주는식)
        check_alpha_number[alpha_idx]  =  check_alpha_number[alpha_idx] + 1
        if(check_alpha_number[alpha_idx] >1):#만약 1을 넘어간다면 중복되는 알파벳이 키에 있다는 뜻이므로 에러메세지를 출력하게 합니다
            print("There are overlapping alphabet in key ")
    print("this key is safe for Substitution_Encryprion")# 아닌경우에는 치환암호를 구현할 key에 적합하다고 출력해줍니다
    return

def Key_generation():#알파벳 26개를 이용해서 키를 랜덤으로 만들어주는 함수입니다.
    temp = list() # random함수는 문자열에서 사용이 불가능 하니까 list를 이용하려고 변수를 넣었습니다.
    for i in Alphabet:# temp list에 알파벳을 하나씩 추가시킵니다.
        temp.append(i)
    random.shuffle(temp) #random.suffle함수를 이용해서 temp list에 있는 26개를 무작위로 섞어줍니다.
    usrkey = ''
    for j in temp:#usrkey를 선언하고 무작위로 섞인 값들을 대입시켜줍니다.
        usrkey += j
    return usrkey


Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "UVGHQRYIAEBCDSTJKLWOPXFMNZ"

plaintxt = "hello world!"
recovered_msg = ''
ciphertxt = ''

ciphertxt = Substitution_En(key,plaintxt)
recovered_msg = Substitution_De(key,ciphertxt)

# print("plain_txt = " , plaintxt)
# print("cipher_txt = " , ciphertxt)
# print("recovered_txt = " , recovered_msg)


#! ---------- consider Key validation
#! ---------- 키를 누가 잘못쓰면 어떡하냐는거지. 알파벳을 섞어서 만들었는데 키가 잘만들어져 있는지 확인을 해봐야함
#* ---------- Random Key Generation
#* ---------- 랜덤키를 하나 만드러주는 함수 만들기(못외울것을 던져준다)
#? File encrypt/decrypt 암호화 복호화
