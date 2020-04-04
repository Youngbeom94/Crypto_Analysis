# -------------------------------
# 암호분석 2020.04.04, 20175204김영범
# -------------------------------

def encrypt(key,msg):
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

def decrypt(key,msg):
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

ciphertxt = encrypt(key,plaintxt)
recovered_msg = decrypt(key,ciphertxt)

print("plain_txt = " , plaintxt)
print("cipher_txt = " , ciphertxt)
print("recovered_txt = " , recovered_msg)


#! ---------- consider Key validation
#! ---------- 키가 입력이 되면 키가 validation 되면 