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

# my_list = ['AES' , 'ARIA', 'LEA', 'SEED', 'Misty']

# print(my_list[:-1])

# my_list += ['Speck','simon']
# print(my_list)

# my_list.append("RSA")
# my_list.append("DES")
# print(my_list)

# if 'LEA' in my_list:
#     print('LEA is iso standard cipher')
# else:
#     print("NO!!")

# for cipher in my_list:
#     print('%s is a block cipher' %(cipher))

# for i in range(0,6):
#     print("%s is cipher" %(my_list[i]))
   

#? 바이트 표현

#------------------------------------------------
# a = 'A'
# # print(a)
# a = ord('A') # a = 65 ; order
# a = chr(a) # a = 'A'  ; character
# # print(a)

#------------------------------------------------

# ch1 = 'A'
# num1 = ord(ch1)
# hex1 = hex(num1) #! hex로 변환된것은 문자열임을 주의하기
# num2 = '65'

# list1 = []
# list1.append(ch1)
# list1.append(num1)
# list1.append(hex1)
# list1.append(num2)

# print(list1)
# print(len(hex1))
#------------------------------------------------

# list2 = []
# num2 = 66
# ch2 = chr(num2)
# hex2 = hex(num2)
# numch2 = '66'

# list2.append(num2)
# list2.append(ch2)
# list2.append(hex2)
# list2.append(numch2)

# print(ch2)
# print(hex2)
# print(list2)

#------------------------------------------------

# list3 = []
# hex3 = '0x43'
# num3 = int(hex3,16)
# ch3 = chr(num3)

# list3.append(num3)
# list3.append(ch3)
# list3.append(hex3)

# print(ch3)
# print(hex3)
# print(list3)

#------------------------------------------------

# str1 =  'ABCD'

# list1 = [ch for ch in str1]
# print(list1)

# list2 =[ord(ch) for ch in str1 ]
# print(list2)

# list3 = list(str1)
# print(list3)

# str2 = ''.join(list1)
# print(str2)

# #* vs  ..what different python and Clang
# list4 = []

# for i in range(len(str1)):
#     list4.append(str1[i])
# print(list4)



#? 문자열 <--->바이트열 <---> 리스트 --> 암복호화

# list5 = [65 , 66, 67, 68]
# bytes1 = bytes(list5) #바이트열을 만드는 함수
# print('bytes1 = ', bytes1)
# str4 = bytes1.decode('ascii')
# # str4 = bytes1.decode('utf8')
# print('str4 =' , str4)

#문자열은 ASCII 문자로 구성된 배열
#바이트열은 바이트로 구성된 배열 : char 배열이라고 생각하는게 편할듯 바이트열은 다 표현가능한데, 바이트열을 문자열로 바꿀때 string으로 매핑이 안될 수 있다. 
#encode : 문자열 -> 바이트열
#decode : 바이트열 -> 문자열


#----------------------------------------------------------
# list1 = [65 , 66, 67, 68]
# bytes1 = bytes(list1)
# str1 = bytes1.decode("utf8")

# # print(list1)
# # print(bytes1)
# # print(str1)

# str2 = 'EFGH'
# bytes2 = bytes(str2,'utf8') #ord(ch) #! I/O 파일 입출력에서는 바이트열을 기준으로 하는게 제일 좋을 듯 하다.
# bytes3 = str2.encode('utf8')
# list2 = list(bytes2)
# list3 = list(str2)

# print(str2)
# print(bytes2)
# print(bytes3)
# print(list2)
# print(list3)

#--------------------------------------------------
# list1 = [1,2,3,4,65 , 66, 67, 68]
# bytes1 = bytes(list1)

# f = open('test-0413.txt','w+b') # binary file
# f.write(bytes1)
# f.close

# list2 = ['a','b','c','d']
# str2 = ''.join(list2)
# f = open('test-0413.txt','w') # binary file
# f.write(str2)
# f.close