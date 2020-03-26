# -------------------------------
# 암호분석 2020.03.26, 20175204김영범
# -------------------------------

#? --연산자 +,
# print ('hello world\n')

# print("Hello" + " world")

# print("hello"*5)

#?--인덱싱
# msg = "Hello, python!"
# print(msg)
# print(msg[0])
# print(msg[-1])
# print(msg[0:5]) #0,1,2,3,4
# print(msg[-7:-1])
# print(msg[:-1])
# print(msg[:-1][-6:])
# print(msg[7:-1])

#?--사용자 입력 받기
# print("Whar is your name?")
# myname = input()
# print("nice to meet you, " + myname+ ".")

#?--len(), find()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alphabet[0:26])
# print(len(alphabet))
# print(alphabet.find("xyz"))
# print(Upper[alphabet.find("o"):])

#?--Reversing 
# msg_txt = "this is a plain txt"
# rev_txt = ""
# i = len(msg_txt) - 1
# while i >= 0:
#     rev_txt = rev_txt + msg_txt[i]
#     i -= 1
# print("Message = " + msg_txt)
# print("Reverse Message = " + rev_txt)


#?--나머지 연산자 %
# print(5 % 3)
# print(5 + 5 % 3)
# print((5 + 5) % 3)


#?--Call by object
x = 10
def ref_demo(x):
    print ("2 x=" ,x," id = ", id(x))
    x = 42
    print ("3 x=" ,x," id = ", id(x))

x = 10
print ("1 x=" ,x," id = ", id(x))
ref_demo(x)
print ("4 x=" ,x," id = ", id(x))
