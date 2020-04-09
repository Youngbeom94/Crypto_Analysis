# -------------------------------
# 암호분석 2020.04.04, 20175204김영범
# -------------------------------

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

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "UVGHQRYIAEBCDSTJKLWOPXFMNZ"

plaintxt = "hello world!"
recovered_msg = ''
ciphertxt = ''

ciphertxt = Substitution_En(key,plaintxt)
recovered_msg = Substitution_De(key,ciphertxt)

print("plain_txt = " , plaintxt)
print("cipher_txt = " , ciphertxt)
print("recovered_txt = " , recovered_msg)


#! ---------- consider Key validation
#! ---------- 키를 누가 잘못쓰면 어떡하냐는거지. 알파벳을 섞어서 만들었는데 키가 잘만들어져 있는지 확인을 해봐야함
#* ---------- Random Key Generation
#* ---------- 랜덤키를 하나 만드러주는 함수 만들기(못외울것을 던져준다)
#? File encrypt/decrypt 암호화 복호화
