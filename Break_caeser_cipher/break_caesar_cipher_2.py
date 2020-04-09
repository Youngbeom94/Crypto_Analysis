#!  파일 입출력 ----------------------------------------------------------
import os, sys
import Caesar_Cipher_func
import english_diclib

ciphertxt = 'Znoy oy g ygsvrk'

for key in range(0,26):
    recovered_msg = Caesar_Cipher_func.caesar_decrypt(key,ciphertxt)
    PercentEngWords = english_diclib.percentEnglishWord(recovered_msg) * 100
    print('key #%2s : %s(English word : %5.1f%%)' %(key, recovered_msg,PercentEngWords))




# in_file = 'my_cipher.txt'
# if not os.path.exists(in_file):
#     print('File %s does not exist' %(in_file))
#     sys.exit()

# Infileobj = open(in_file)
# my_cipher = Infileobj.read()
# Infileobj.close()
# print(my_cipher)

# key = 13
# my_new_text = Caesar_Cipher_func.caesar_decrypt(key,my_cipher)

# print(my_cipher)
# key = 13
# my_cipher = Caesar_Cipher_func.caesar_encrypt(key,my_cipher)



# out_file = 'my_new_text.txt'
# if os.path.exists(out_file):
#     print('this will overwite te file %s  C or Q' %(out_file))
#     response = input('---->')
#     if not response.lower().startswith('c'):
#         sys.exit()

# outfileobj = open(out_file,'w')
# outfileobj.write(my_new_text)
# outfileobj.close()
