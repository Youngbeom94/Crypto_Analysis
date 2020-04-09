# -------------------------------
# 암호분석 2020.03.26, 20175204김영범
# -------------------------------

#!-- dictionary (key, value) sample


myDic1 = {'us' : 'AES','kr' : 'LEA', 'jp' : 'MISTY'}
print(myDic1['kr'])

#--copy
myDic2 = myDic1
myDic2['ru'] = 'GOST'
print(myDic1)
print(myDic2)

# #--Deep copy
import copy
myDic3 = copy.deepcopy(myDic1)
myDic3['uk'] = 'IDEA'
print("mydic1 = ", myDic1)
print("mydic3 = ", myDic3)

#--- dictionary
for element in myDic3:
    print(element, myDic3[element])     #key, value

#---------------------------------------------------

msg = 'This is a sample text'
list_msg = msg.split()
print('msg = ',  msg)
print('list =' , list_msg) #! 단어 분리

joined_msg = ''.join(list_msg)
print('joined = ',joined_msg)

for k in range(len(list_msg) - 1):
    list_msg[k] += ' '

joined_msg2 = ''.join(list_msg)
print('joined = ',joined_msg2)


# #!------------sampl