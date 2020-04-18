#-------------------------
# 암호분석 2020 20175204김영범
#-------------------------
import TC20_Dec_lib
import TC20_Enc_lib
import string 
import random 

def Make_Random_String(len):
    string_pool = string.ascii_letters # 소문자 
    string_digits = string.digits
    random_string = "" #message 임의로 생성
    for i in range(len) : 
        random_string += random.choice(string_pool) # 랜덤한 문자열 하나 선택 print(result)​
    return random_string

def Run_TC20(msg,key):
    input_state = [ord(ch) for ch in msg]
    output_state = [item for item in TC20_Enc_lib.TC20_Enc(input_state, key)]
    Cipher_message = [chr(num) for num in output_state]
    Recovered_state = [item for item in TC20_Dec_lib.TC20_Dec(output_state, key)]
    Recovered_char_list = [chr(num) for num in Recovered_state]
    Recovered_message = ''.join(Recovered_char_list)
    return Cipher_message , Recovered_message


#------------------------------------------------
def main():
    len = 4
    message = Make_Random_String(len)
    key = [0, 1, 2, 3]
    Cipher_message , Recovered_message = Run_TC20(message,key)

    print('message =', message)                    
    print('Cipher_message =', Cipher_message)      
    print('Recovered_message =', Recovered_message)
##-- Run main()
if __name__ == '__main__':
    main()