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
# x = 10
# def ref_demo(x):
#     print ("2 x=" ,x," id = ", id(x))
#     x = 42
#     print ("3 x=" ,x," id = ", id(x))

# x = 10
# print ("1 x=" ,x," id = ", id(x))
# ref_demo(x)
# print ("4 x=" ,x," id = ", id(x))

#?--inplace operation
#! 함수로 전달된 파라미터의 값은 바뀔 수 있는가?
#! immutable variable vs Mutable variable

# in-place operation은 새로 메모리를 할당하지 않고 기존 데이터를 업데이트함
    # 원래있던 벡터자리 그대로 숫자를 업데이트 함
    # find deferent of + vs +=



#! check plz
# def my_func_0(a):
#     print("2 a = ",a, "id  = ",id(a))
#     a = a + 1
#     print("3 a = ",a, "id  = ",id(a))



# a = 10
# print("1 a = ",a, "id  = ",id(a))
# my_func_0(a)
# print("4 a = ",a, "id  = ",id(a))

# '''
#     1 a =  10 id  =  4404924368
#     2 a =  10 id  =  4404924368
#     3 a =  11 id  =  4404924400
#     4 a =  10 id  =  4404924368
# '''

# def my_swap(a,b):
#     print('a = ',a, 'b = ', b)
#     temp = a
#     a = b
#     b = temp
#     print('a = ',a, 'b = ', b)
#     return a,b

# x = 10
# y = 20
# print('x = ',x, 'y = ', y)
# # x,y = my_swap(x,y)
# x,y = y,x
# print('x = ',x, 'y = ', y)

#??---List

my_list = ['AES' , 'ARIA', 'LEA', 'SEED', 'Misty']

# print(my_list[:-1])

my_list += ['Speck','simon']
# print(my_list)

my_list.append("RSA")
my_list.append("DES")
# print(my_list)

# if 'LEA' in my_list:
#     print('LEA is iso standard cipher')
# else:
#     print("NO!!")

for cipher in my_list:
    print('%s is a block cipher' %(cipher))

