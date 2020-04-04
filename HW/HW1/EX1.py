# -------------------------------
# 암호분석 2020.04.04, 20175204김영범
# HW1
# -------------------------------

'''
    Ex1.py
    암호키에 대한 유효성을 확인하는 함수를 작성하고, 이를 이용하여 암호화 복호화 하는 예제를 제시해라
'''

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


#---------------선 언------------------------
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "UVGHQRYIAEBCDSTJKLWOPXFMNZ"
plaintxt = "hello world!"
ciphertxt = ''
recovered_msg = ''

def main():
#---------------Encrypt and Decrypt-----------
    Key_Validation(key)
    ciphertxt = Substitution_En(key,plaintxt)
    recovered_msg = Substitution_De(key,ciphertxt)
#---------------Print msg-----------
    print("plain_txt = " , plaintxt)
    print("cipher_txt = " , ciphertxt)
    print("recovetxt = " , recovered_msg)


if __name__ == '__main__': 
    main()
