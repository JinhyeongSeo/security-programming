from AES_Test_New import aesEncrypt, aesDecrypt
from Crypto.Hash import SHA512

def gen_Key_IV(seed):
    hash = SHA512.new()
    hash.update(seed.encode('utf-8'))
    key = hash.digest()
    key = key[16:48] # AES Key 값: seed에 대한 SHA512 해시 값의 16 바이트 ~ 47 바이트(32*8 = 256비트) 까지의 값을 이용함
    print("key:", key.hex())
    iv = hash.digest()
    iv = iv[:16]   # AES IV 값 : seed에 대한 SHA512 해시 값의 0 바이트 ~ 15 바이트(16*8 = 128비트) 까지의 값을 이용함
    print("IV:", iv.hex())
    return key, iv

def main():
    seed = "2022-2 Security Programming"
    msg = "Python Programming"
    key, iv = gen_Key_IV(seed)
    ciphertext = aesEncrypt(msg.encode(), key, iv)
    print("ciphertext: ", ciphertext.hex())
    print("ciphertext: ", ciphertext)
    plaintext = aesDecrypt(ciphertext, key, iv)
    print("plaintext: ", plaintext.decode())

if __name__ == "__main__":
    main()
