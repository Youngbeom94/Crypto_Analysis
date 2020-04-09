# -------------------------------
# 암호분석 2020.03.26, 20175204김영범
# -------------------------------

#!Casar Cipher
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#?---Plaintxt
plain_msg = "this is a plaintext message to be encrypted!"

#?---key
key = 3 # key must be in [0..25]

#?---Encrypt
cipher_msg = ""

for symbol in plain_msg: #plainmsg 안에서 하나씩 가져오겠다?
    if symbol in upper_alphabet:
        symbol_idx = upper_alphabet.find(symbol)
        trans_idx = (symbol_idx + key) % len(upper_alphabet)
        cipher_msg = cipher_msg + upper_alphabet[trans_idx]
    elif symbol in lower_alphabet:
        symbol_idx = lower_alphabet.find(symbol)
        trans_idx = (symbol_idx + key) % len(lower_alphabet)
        cipher_msg = cipher_msg + lower_alphabet[trans_idx]
    else: #-- 영문자가 아닌경우
        cipher_msg = cipher_msg + symbol

print("plain txt = ",plain_msg )
print("cipher txt = ",cipher_msg )

#?---Decrypt
recovered_msg = ""

for symbol in cipher_msg: #plainmsg 안에서 하나씩 가져오겠다?
    if symbol in upper_alphabet:
        symbol_idx = upper_alphabet.find(symbol)
        trans_idx = (symbol_idx - key) % len(upper_alphabet)
        recovered_msg = recovered_msg + upper_alphabet[trans_idx]
    elif symbol in lower_alphabet:
        symbol_idx = lower_alphabet.find(symbol)
        trans_idx = (symbol_idx - key) % len(lower_alphabet)
        recovered_msg = recovered_msg + lower_alphabet[trans_idx]
    else: #-- 영문자가 아닌경우
        recovered_msg = recovered_msg + symbol

print("\n")
print("plain txt = ",plain_msg )
print("cipher txt = ",cipher_msg )
print("recovered txt = ",recovered_msg )
    
# <<< 실습 >>>


