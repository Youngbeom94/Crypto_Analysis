# -------------------------------
# 암호분석 2020.03.26, 20175204김영범
# -------------------------------

# ! liblary 만든것임
import os, sys
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_and_space = upper_alphabet + upper_alphabet.lower() + '\t\n' #tap 공백 추가

def loaddictionary():
    dictionary_file = open('dictionary.txt')
    Englishwords = {}
    for word in dictionary_file.read().split('\n'):
        Englishwords[word] = None
    dictionary_file.close()
    return Englishwords

#--전역변수
Englishwords = loaddictionary() #전역변수에 dictionary 파일을 집어넣는다

#------특수문자, 숫자 지우기(message에서 공백과 특수문자 제거해주기)
def removNonletters(message):
    letters_only = []
    for ch in message:
        if ch in letter_and_space:
            letters_only.append(ch)
    return ''.join(letters_only)

#---------------------- 올바른 영어단어의 비율(percent )
def percentEnglishWord(message):
    message = message.lower()
    message = removNonletters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0
    count_words = 0
    for word in possible_words:
        if word in Englishwords:
            count_words += 1
    return float(count_words)/len(possible_words)

#def--------------------- 영어인지 판정하기
def isenglish(message,WordPercentage = 20, letterPercentage = 80):
    wordsMatch = percentEnglishWord(message) * 100 >= WordPercentage

    numLetters = len(removNonletters(message))
    MessageletterPercentage = float(numLetters) / len(message) * 100
    lettersMatch = MessageletterPercentage >= letterPercentage

    return wordsMatch and lettersMatch
