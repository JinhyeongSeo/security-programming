from Crypto.Cipher import AES
import random
from detectEnglish import  isEnglish
import time


def aesEncrypt(message, key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.encrypt(message)


def aesDecrypt(encrypted, key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.decrypt(encrypted)


def aesKeyGen(zerovalue_length, salt = '0123456789abcdef',KEY_SIZE=32):
    key32 = "".join(['0' if i <= zerovalue_length-1 else salt[random.randrange(0, len(salt))] for i in range(KEY_SIZE)])
    bruteForceKey32 = str(key32).encode('utf-8')
    return bruteForceKey32


def genAesKeyHex(val, KEY_SIZE=32):
    zeroString = "0" * (KEY_SIZE - len(str(hex(val)[2:])))
    bruteForceKey32 = zeroString + hex(val)[2:]
    bruteForceKey32 = str(bruteForceKey32).encode('utf-8')
    return bruteForceKey32


def aesHack(encrypted, iv, zerovalue_length):
    while (True):
        bruteForceKey32 = aesKeyGen(zerovalue_length)
        decrypted = aesDecrypt(encrypted, bruteForceKey32, iv)
        if (isEnglish(str(decrypted))):
            print("English Sentences!!!")
            print("AES Key Found!!!")
            print("AES Key :", bruteForceKey32.decode())
            print("decrypted: ", decrypted.decode())
            break


### 순차적으로 키를 생성하면서 복호화 과정을 수행하는 방식
def aesHack2(encrypted, iv, zerovalue_length):
    KEY_SIZE = 32
    flag = False
    key_start = 0
    key_end = "f" *(KEY_SIZE-zerovalue_length)
    for val in range(key_start, int(key_end,base=16)+1):
        bruteForceKey32 = genAesKeyHex(val)
        decrypted = aesDecrypt(encrypted, bruteForceKey32, iv)
        if (isEnglish(str(decrypted))):
            print("English Sentences!!!")
            print("AES Key Found!!!")
            print("AES Key :", bruteForceKey32.decode())
            print("decrypted: ", decrypted.decode())
            flag = True
            break
    if not flag:
        print("Brute Force AES Key Fail!!!")


def calcTime(start_time, end_time, random_key_length, KEY_SIZE=32):
    run_time = (end_time-start_time) * pow(16, (KEY_SIZE-random_key_length))
    sec = run_time % 60
    min = (run_time / 60) %60
    hour = (run_time / (60*60)) %24
    day = (run_time / (60*60*24))  % 365
    year =(run_time / (60*60*24*365))
    return year, day, hour, min, sec


def main():
    ## AES Encryption
    BLOCK_SIZE = 16
    KEY_SIZE = 32
    random_key_length = 4
    zerovalue_length = KEY_SIZE - random_key_length      ### 만일 zerovalue_length = 28 이면 b'00000000000000000000000000008e6e' 와 같이 앞 28개가 0으로 채워짐
    message = b"Information Security Programming Test Message Hanshin University Computer Science."
    print("plaintext: ", message.decode())
    iv = b"0000000000123456"  ## iv 값 고정
    print("IV: ", iv)
    randKey32 = aesKeyGen(zerovalue_length)
    print("random generated AES key: ", randKey32)
    encrypted = aesEncrypt(message, randKey32, iv)
    print("Encrypted: ", encrypted)
    print("Encrypted(hex): ", encrypted.hex())

    ## AES Hack with Decryption
    print("\nDecryption using isEnglish Function!!!")
    start_time = time.time()
    aesHack(encrypted, iv, zerovalue_length)
    end_time = time.time()
    print(f"{end_time-start_time:.5f} sec")
    start_time = time.time()
    aesHack2(encrypted, iv, zerovalue_length)
    end_time = time.time()
    print(f"{end_time - start_time:.5f} sec")
    #year, day, hour, min, sec = calcTime(start_time, end_time, random_key_length)
    #print("Full Random 265bits AES Key Brute Force Time : %d 년 %d 일 %d 시간 %d 분 %d 초 " %(year, day, hour, min, sec))
    print("Full Random 265bits AES Key Brute Force Time : %d 년 %d 일 %d 시간 %d 분 %d 초 " %(calcTime(start_time, end_time, random_key_length)))

if __name__ == "__main__":
    main()
