import string
import random

#encryption
def substituteEncryption(plaintext,dict1,LETTERS):
    ciphertext = ""
    for char in plaintext:
        if char in LETTERS:
            temp = dict1[char] #dict1 의 key에 해당하는 value 추출
            ciphertext += temp
        else:
            ciphertext += char

    return ciphertext

#decryption
 #key, value 순서를 바꿈
def substituteDecryption(ciphertext,dict1,LETTERS):
    dict1_swap = {value:key for key,value in dict1.items()}
    print(dict1_swap) # decryption decryption key
    decrypted = ""
    for char in ciphertext:
        if char in LETTERS:
            temp = dict1_swap[char] #dict1 의 key에 해당하는 value 추출
            decrypted += temp
        else:
            decrypted += char

    return decrypted

if __name__ == "__main__":
    LETTERS = string.ascii_lowercase + string.ascii_uppercase
    print(LETTERS)
    dict1 = {}
    shuffle_LETTERS = "".join(random.sample(LETTERS, len(LETTERS)))
    print(shuffle_LETTERS)
    for i in range(len(LETTERS)):
        dict1[LETTERS[i]] = shuffle_LETTERS[i]
    print(dict1)

    #user input plaintext
    plaintext = input("Input plaintext : ")

    #encryption
    ciphertext = substituteEncryption(plaintext,dict1,LETTERS)
    print("ciphertext is : ",ciphertext)
    #decryption
    decrypted = substituteDecryption(ciphertext,dict1,LETTERS)
    print("decrypted plaintext is : ", decrypted)