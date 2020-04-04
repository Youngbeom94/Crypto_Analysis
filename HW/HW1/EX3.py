# -------------------------------
# 암호분석 2020.04.04, 20175204김영범
# HW3
# -------------------------------
import EX1
import EX2
import os   # 파일 입출력을 위한 import입니다.
import sys  

'''
    Ex3.py
    텍스트 파일에서 평문을 읽어 암호문 파일을 만드는 예제와 이를 복호화하는 예제를 작성하라.
'''
#---------------my test 파일 입력------------------
in_file = 'my_text.txt'
if not os.path.exists(in_file):
    print('File %s does not exist' % (in_file))
    sys.exit()

Infileobj = open(in_file)
plaintxt = Infileobj.read()
Infileobj.close()

#---------------선 언---------------------------
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ''
ciphertxt = ''
recoverd_txt = ''

#----------Key_generation and Encrypt-----------
key = EX2.Key_generation()
EX1.Key_Validation(key)
ciphertxt = EX1.Substitution_En(key, plaintxt)

#---------------Print msg---------------------
print("key           = ", key)

#--------------Write msg 출력----------------------
out_file = 'my_cipher_msg.txt'
# if os.path.exists(out_file):     #기존 파일이 있는경우 발생하는 경고 메세지 실제 실행할땐 없어도 됩니다.
#     print('already exit file')
#     sys.exit()
outfileobj = open(out_file,'w')
outfileobj.write(ciphertxt)
outfileobj.close()


#-------------- decrption----------
#만들어 놓은 cipher msg를 이용해서 recoverd msg를 만들고 file에 write 하는 함수
recoverd_txt = EX1.Substitution_De(key,ciphertxt)  
out_file = 'recovered_msg.txt'
# if os.path.exists(out_file):
#     print('already exit file')
#     sys.exit()
outfileobj = open(out_file,'w')
outfileobj.write(recoverd_txt)
outfileobj.close()


