# -------------------------------
# 암호분석 2020.03.26, 20175204김영범
# -------------------------------

#!Casar Cipher
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#-- Caesar 암호화
def caesar_encrypt(key,plain_msg):
    cipher_msg = ''
    for symbol in plain_msg:
        if symbol in upper_alphabet:
            symbol_idx = upper_alphabet.find(symbol)
            cipher_msg  = cipher_msg + upper_alphabet[(symbol_idx + key) % len(upper_alphabet)]
        elif symbol in lower_alphabet:
            symbol_idx = lower_alphabet.find(symbol)
            cipher_msg  = cipher_msg + lower_alphabet[(symbol_idx + key) % len(lower_alphabet)]
        else:
            cipher_msg = cipher_msg + symbol
    return cipher_msg

def caesar_decrypt(key,plain_msg):
    recorvedtxt = ''
    for symbol in plain_msg:
        if symbol in upper_alphabet:
            symbol_idx = upper_alphabet.find(symbol)
            recorvedtxt  = recorvedtxt + upper_alphabet[(symbol_idx - key) % len(upper_alphabet)]
        elif symbol in lower_alphabet:
            symbol_idx = lower_alphabet.find(symbol)
            recorvedtxt  = recorvedtxt + lower_alphabet[(symbol_idx - key) % len(lower_alphabet)]
        else:
            recorvedtxt = recorvedtxt + symbol
    return recorvedtxt

#!-- 테스트용 main()
def main():
    plaintxt = "This is plain txt!!"
    Ciphertxt = ''
    recorvedtxt = ''
    key = 3

    Ciphertxt = caesar_encrypt(key,plaintxt)
    recorvedtxt = caesar_decrypt(key,Ciphertxt)
    print("Cipher txt = " , plaintxt)
    print("plain txt = " ,Ciphertxt)
    print("recover txt = ", recorvedtxt)


#---- Run main()
if __name__ == '__main__': # 만약 다른 함수에서 실행하면 실행하지 말라
    main()