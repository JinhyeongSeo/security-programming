import string
import random

#LETTERS = string.ascii_lowercase + string.ascii_uppercase
LETTERS = string.ascii_letters
print(LETTERS)

key = random.randrange(0,len(LETTERS))

plaintext = "Hello World"

#caesarEncryption
ciphertext = ""
for char in plaintext:
    if char in LETTERS:
        ciphertext += LETTERS[(LETTERS.find(char) + key) % len(LETTERS)]
    else:
        ciphertext += char

print(ciphertext)
#caesarDecryption
#ciphertext,key,LETTERS
decrypt = ""
for char in ciphertext:
    if char in LETTERS:
        decrypt += LETTERS[(LETTERS.find(char) - key) % len(LETTERS)]
    else:
        decrypt += char

print(decrypt)