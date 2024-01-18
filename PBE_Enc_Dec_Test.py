import binascii

from Crypto import Random
from Crypto.Hash import SHA512
from Crypto.Cipher import AES

SALT_SIZE = 16
BLOCK_SIZE = 16
KEY_SIZE = 32

def inputPW():
    password = input("Input Password: ").encode('utf-8')
    return password


def inputPT():
    plaintext = input("Input Plaintext: ").encode('utf-8')
    return plaintext


def generateKEK(salt, alicePassword):
    KEK = ""
    temp = salt + alicePassword
    h = SHA512.new()
    h.update(temp)
    KEK = h.digest()
    print("key KEK: ", KEK.hex())
    return KEK[:KEY_SIZE] ### 전체 512비트 --> 그중에서 256비트 32바이트만 사용함


def generateCEK():
    CEK = ""
    CEK = Random.new().read(KEY_SIZE)
    return CEK

def aesEncrypt(message, key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.encrypt(message)

def aesEncForMSG(alicePlaintext, CEK, iv):
    ciphertext = aesEncrypt(alicePlaintext, CEK, iv)
    return ciphertext


def aesEncForCEK(CEK, KEK, iv):
    encCEK = aesEncrypt(CEK, KEK, iv)
    return encCEK


def aesDecrypt(encrypted, key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.decrypt(encrypted)


def aesDecForCEK(encryptedCEK, KEK, iv):
    CEK = aesDecrypt(encryptedCEK, KEK, iv)
    return CEK


def Store_USB(salt, encCEK, iv, encPlaintext, message):
    filename = input("USB stored Filename(ex: PBE_Store.enc):") or "PBE_Store.enc"
    f = open(filename, 'wt')
    """
        salt + encrypted CEK + iv + encPlaintext
    """
    hpk = binascii.hexlify(salt) + '$*****$'.encode('utf8') \
          + binascii.hexlify(encCEK) + '$*****$'.encode('utf8') \
          + binascii.hexlify(iv) + '$*****$'.encode('utf8') \
          + binascii.hexlify(encPlaintext) + '$*****$'.encode('utf8') \
          + binascii.hexlify(SHA512.new(message).digest())
    print("salt & encrypted CEK & iv & ciphertext :", hpk)
    f.write(hpk.decode('utf-8'))
    f.close()

def Read_USB():
    filename = input("USB Stored Filename(ex: PBE_Store.enc): ")
    f = open(filename,'r')
    salt, encCEK, iv, encPlaintext, hashValue = f.readline().split("$*****$")
    salt = bytearray.fromhex(salt)
    encCEK = bytearray.fromhex(encCEK)
    iv = bytearray.fromhex(iv)
    encPlaintext = bytearray.fromhex(encPlaintext)
    hashValue = bytearray.fromhex(hashValue)
    f.close()
    return salt,encCEK,iv,encPlaintext,hashValue

def PBE_Encrypt():
    # password inpt
    alicePassword = inputPW()
    # plaintext input
    alicePlaintext = inputPT()
    # SHA generate --> generate KEK
    salt = Random.new().read(SALT_SIZE)
    KEK = generateKEK(salt, alicePassword)   # input : salt, alicePassword output : KEK
    # using random --> generate CEK
    CEK = generateCEK()
    # message AES Encryption using CEK
    iv = Random.new().read(BLOCK_SIZE)
    encPlaintext =  aesEncForMSG(alicePlaintext, CEK, iv)   # parameter 1: 암호의 대상, parameter 2: 사용하는 키, parameter 3: iv
    # CEK AES Encryption using KEK
    encCEK = aesEncForCEK(CEK, KEK, iv)
    # Generate File on USB
    Store_USB(salt, encCEK, iv, encPlaintext, alicePlaintext)

def PBE_Decrypt():
    # alicePassword input
    alicePassword = inputPW()

    # Read from USB --> split
    salt, encCEK, iv, encPlaintext, hashValue = Read_USB()

    # KEK Generate
    KEK = generateKEK(salt, alicePassword)

    # encrypted CEK --> Decryption
    CEK = aesDecForCEK(encCEK, KEK, iv)

    # encrypted MSG --> Decryption
    plaintext = aesDecrypt(encPlaintext, CEK, iv)
    SHA512.new(plaintext).digest()
    if (SHA512.new(plaintext).digest() == hashValue):
        print("Integrity OK")
    else:
        print("corrupted")
    return plaintext

def main():

    PBE_Encrypt()
    output = PBE_Decrypt()
    print("Final Message: %s" % output.decode('utf-8'))

if __name__ == "__main__":
    main()