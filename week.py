# -------------------------------
# 암호분석 2020.04.09, 20175204김영범
# -------------------------------

import Substitution_Cipher_lib
import os, sys

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVJXQZ' #?영어에서 가장많이 사용하는 알파벳 빈도순서
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#-------------------------------------------------------------------------------------------
def getletterCount(msg): #알파벳 빈도수 측정 함수
    letterCount = { 'A' : 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
                'I': 0 , 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
                'Q': 0 , 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                'Y': 0, 'Z': 0} #? 파이썬 dictionary 타입 'A'에는 0이 들어있고 'B'에는 0이들어있고...
    for char in msg.upper():
        if char in LETTERS: 
            letterCount[char] += 1
    return letterCount

def getitemZero(items): # i , items = (key,value) = (items[0], items[1]) -->key return 함수
    return items[0] 

def getFreqorder(msg):# 알파벳 빈도순으로 문자열 만들기
    letter_freq_dic = getletterCount(msg) # =  {A : 10, B = 4, ....,Z = 33}
    freq_leeter_dic = {} # we need to dic as {10 : 'AVC', 4 : B}... 동점자도 나올 수 있게 (key,value) = (feq, alpha)
    for char in LETTERS:
        if letter_freq_dic[char] not in freq_leeter_dic: #현재 알파벳의 빈도가 처음 나온 것
            freq_leeter_dic[letter_freq_dic[char]] = [char] #list type
        else :
            freq_leeter_dic[letter_freq_dic[char]].append(char) #list append
    for freq in freq_leeter_dic:
        freq_leeter_dic[freq].sort(key = ETAOIN.find, reverse = False)
        freq_leeter_dic[freq] = ''.join(freq_leeter_dic[freq])

    #빈도 순서대로 정렬하기
    freqpairs = list(freq_leeter_dic.items())
    freqpairs.sort(key = getitemZero, reverse = True)
    freq_order_list = []
    for freq_pair in freqpairs:
        freq_order_list.append(freq_pair[1])

    return ''.join(freq_order_list)



#-------------------------------------------------------------------------------------------
in_file = 'my_text.txt' #입력파일
text = Substitution_Cipher_lib.ReadFile(in_file)
# print(getletterCount(text))
freqletter =  getFreqorder(text)
print("my txt = " ,freqletter)
print("ETATIO = ", ETAOIN)