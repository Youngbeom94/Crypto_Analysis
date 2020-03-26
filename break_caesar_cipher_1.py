# -------------------------------
# 암호분석 2020.03.26, 20175204김영범
# -------------------------------

#!-- caeser cipher library
import Caesar_Cipher_func

# Ciphertxt = "Wklv lv sodlq waw!!"
# print('Cipher is  = ' , Ciphertxt)

# for key in range(0,26):
#     recovered_msg = Caesar_Cipher_func.caesar_decrypt(key,Ciphertxt)
#     print('key #%2s = %s' %(key, recovered_msg))

# #-- 파일 입출력
# import os, sys

# in_file = 'my_text.txt'
# if not os.path.exists(in_file):
#     print('File %s does not exist' %(in_file))
#     sys.exit()

# Infileobj = open(in_file)
# my_content = Infileobj.read()
# Infileobj.close()

# print(my_content)
# key = 13
# my_cipher = Caesar_Cipher_func.caesar_encrypt(key,my_content)




# out_file = 'my_cipher.txt'
# if os.path.exists(out_file):
#     print('this will overwite te file %s  C or Q' %(out_file))
#     response = input('---->')
#     if not response.lower().startswith('c'):
#         sys.exit()

# outfileobj = open(out_file,'w')
# outfileobj.write(my_cipher)
# outfileobj.close()


# ----------------------------------------------------------
import os, sys
in_file = 'my_cipher.txt'
if not os.path.exists(in_file):
    print('File %s does not exist' %(in_file))
    sys.exit()

Infileobj = open(in_file)
my_cipher = Infileobj.read()
Infileobj.close()
print(my_cipher)

key = 13
my_new_text = Caesar_Cipher_func.caesar_decrypt(key,my_cipher)

print(my_cipher)
key = 13
my_cipher = Caesar_Cipher_func.caesar_encrypt(key,my_cipher)



out_file = 'my_new_text.txt'
if os.path.exists(out_file):
    print('this will overwite te file %s  C or Q' %(out_file))
    response = input('---->')
    if not response.lower().startswith('c'):
        sys.exit()

outfileobj = open(out_file,'w')
outfileobj.write(my_new_text)
outfileobj.close()