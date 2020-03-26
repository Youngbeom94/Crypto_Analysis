
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

