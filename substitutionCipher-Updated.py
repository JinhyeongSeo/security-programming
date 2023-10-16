import string
import random


def substituteEncryption(all_letters, dict1, plaintext):
    ciphertext = []

    for char in plaintext:
        if char in all_letters:
            temp = dict1[char]
            ciphertext.append(temp)
        else:
            temp = char
            ciphertext.append(temp)

    ciphertext = "".join(ciphertext)
    return ciphertext

## decryption

def substituteDecryption(all_letters, dict1, ciphertext):
    dict1_swap = {v: k for k, v in dict1.items()}
    decrypt = []
    for char in ciphertext:
        if char in all_letters:
            temp = dict1_swap[char]
            decrypt.append(temp)
        else:
            temp = char
            decrypt.append(temp)

    decrypt = ''.join(decrypt)
    return decrypt

if __name__ == "__main__":
    all_letters = string.ascii_letters
    shuffled_all_letters = ''.join(random.sample(all_letters,len(all_letters)))

    dict1 = {}
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = shuffled_all_letters[(i)%len(all_letters)]
    print(dict1)
    plaintext = "I am studing Information Security Programming"
    print("Plaintext is :", plaintext)

    ciphertext = substituteEncryption(all_letters, dict1, plaintext)
    print("Ciphertext is : ", ciphertext)
    decrypt = substituteDecryption(all_letters, dict1, ciphertext)
    print("Decrypted text is :", decrypt)