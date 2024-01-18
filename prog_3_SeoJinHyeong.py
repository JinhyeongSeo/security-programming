from Crypto.Hash import SHA512
import binascii
from Crypto.Cipher import AES
from Crypto import Random
def inputPassword():
    password = input("Input Password for PBE:").encode('utf-8')
    print("Alice's password: %s" % password)
    return password
def readUSB():
    filename = input("USB Stored Filename(ex: PBE_Store.enc):")
    f = open(filename, 'r')
    f.seek(0)
    salt, encryptedCEK, iv, ciphertext = f.readline().split('$*****$')
    salt = bytearray.fromhex(salt)
    encryptedCEK = bytearray.fromhex(encryptedCEK)
    iv = bytearray.fromhex(iv)
    ciphertext = bytearray.fromhex(ciphertext)
    f.close()
    return salt, encryptedCEK, iv, ciphertext
def genKEK(salt, password):
    message = salt + password
    hash_Func = SHA512.new()
    hash_Func.update(message)
    keyKEK = hash_Func.digest()
    print("key KEK: ", keyKEK.hex())
    return keyKEK      # return keyKEK
def decCEK(encryptedCEK, keyKEK, iv):
    keyCEK = aesDecrypt(encryptedCEK, keyKEK[:32], iv)
    return keyCEK
def aesDecrypt(encrypted, key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.decrypt(encrypted)
def PBE_Decryption():
    alicePassword = inputPassword()
    salt, encryptedCEK, iv, ciphertext = readUSB()
    keyKEK = genKEK(salt, alicePassword)
    decryptedCEK = decCEK(encryptedCEK, keyKEK, iv)
    plaintext = aesDecrypt(ciphertext, decryptedCEK, iv)
    print("AES Decrypted plaintext: %s" % plaintext)
    return plaintext

def main():
    plaintext = PBE_Decryption()
    print("Final Message: %s" % plaintext.decode('utf-8'))

if "__main__" == __name__:
    main()