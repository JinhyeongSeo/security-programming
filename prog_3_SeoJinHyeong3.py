import binascii
import sys
from Crypto import Random
from Crypto.Hash import SHA512
from Crypto.Cipher import AES


SALT_SIZE = 16
BLOCK_SIZE = 16
KEY_SIZE = 32  # bytes
class PBE():
    def __init__(self):
        self.alicePassword = ""
        self.alicePasswordDec = ""
        self.salt = ""
        self.KEK = ""
        self.CEK = ""
        self.message = ""
        self.match_count = 0
        self.alicePasswordEnc = ""# 패스워드 일치 횟수를 추적하기 위한 변수
        self.finishDec = 0
    def aesEncrypt(self, message, key, iv):
        cipher = AES.new(key, AES.MODE_OFB, iv)
        return cipher.encrypt(message)

    def aesDecrypt(self, encrypted, key, iv):
        cipher = AES.new(key, AES.MODE_OFB, iv)
        return cipher.decrypt(encrypted)

    def inputPW(self):
        password = input("Input Password: ").encode('utf-8')
        print("Alice's password: %s" % password)
        return password

    def inputPT(self):
        plaintext = input("Input Plaintext: ").encode('utf-8')
        print("Alice's password: %s" % plaintext)
        return plaintext

    def generateKEK(self, salt, alicePassword):
        KEK = ""
        temp = salt + alicePassword
        h = SHA512.new()
        h.update(temp)
        KEK = h.digest()  ### 전체 512비트
        print("key KEK: ", KEK.hex())
        return KEK[:KEY_SIZE]  ### 전체 512비트 --> 그중에서 256비트 32바이트만 사용함

    def generateCEK(self):
        CEK = ""
        CEK = Random.new().read(KEY_SIZE)
        return CEK

    def aesEncForMSG(self, alicePlaintext, CEK, iv):
        ciphertext = self.aesEncrypt(alicePlaintext, CEK, iv)
        return ciphertext

    def aesEncForCEK(self, CEK, KEK, iv):
        encCEK = self.aesEncrypt(CEK, KEK, iv)
        return encCEK

    def aesDecForCEK(self, encryptedCEK, KEK, iv):
        CEK = self.aesDecrypt(encryptedCEK, KEK, iv)
        return CEK

    def Store_USB(self, salt, encCEK, iv, encPlaintext):
        filename = input("USB Stored Filename(ex: PBE_Store.enc):") or "PBE_Store.enc"
        f = open(filename, 'wt')
        """
            salt + encrypted CEK + iv + encPlaintext 
        """
        hpk = binascii.hexlify(salt) + '$*****$'.encode('utf8') \
              + binascii.hexlify(encCEK) + '$*****$'.encode('utf8') \
              + binascii.hexlify(iv) + '$*****$'.encode('utf8') \
              + binascii.hexlify(encPlaintext)
        print("salt & encrypted CEK & iv & ciphertext :", hpk)
        f.write(hpk.decode('utf-8'))
        f.close()

    def Read_USB(self):
        if self.finishDec == 1 :
            sys.exit()
        filename = input("USB Stored Filename(ex: PBE_Store.enc):") or "PBE_Store.enc"
        f = open(filename, 'r')
        # f.seek(0)
        salt, encryptedCEK, iv, ciphertext = f.readline().split('$*****$')
        salt = bytearray.fromhex(salt)
        encryptedCEK = bytearray.fromhex(encryptedCEK)
        iv = bytearray.fromhex(iv)
        ciphertext = bytearray.fromhex(ciphertext)
        print("salt: %s %d " % (salt, len(salt)))
        print("encryptedCEK: %s" % encryptedCEK)
        print("iv: %s %d" % (iv, len(iv)))
        print("ciphertext: %s" % ciphertext)
        f.close()
        return salt, encryptedCEK, iv, ciphertext

    def PBE_Encrypt(self):
        # password input
        alicePassword = self.inputPW()
        self.alicePasswordEnc = alicePassword
        # plaintext input
        alicePlaintext = self.inputPT()
        # SHA generate --> generate KEK
        salt = Random.new().read(SALT_SIZE)
        KEK = self.generateKEK(salt, alicePassword)  # input : salt, alicePassword  output : KEK
        # using random --> generate CEK
        CEK = self.generateCEK()
        # message AES Encryption using CEK
        iv = Random.new().read(BLOCK_SIZE)
        encPlaintext = self.aesEncForMSG(alicePlaintext, CEK, iv)  # parameter 1: 암호화 대상, 파라메터 2 : 사용하는 키, 패라메터 3 : IV
        # CEK AES Encryption using KEK
        encCEK = self.aesEncForCEK(CEK, KEK, iv)  # parameter 1: 암호화 대상, 파라메터 2 : 사용하는 키, 패라메터 3 : IV
        # Generate File on USB
        self.Store_USB(salt, encCEK, iv, encPlaintext)
        return encPlaintext

    def PBE_Decrypt(self):
        # password input
        if self.finishDec == 1:
            sys.exit()
        alicePassword = self.inputPW()
        self.alicePasswordDec = alicePassword
        if self.alicePasswordDec != self.alicePasswordEnc:
            if self.match_count < 2:
                self.match_count += 1
                print("%d번 틀리셨습니다.alicePassword가 틀렸습니다. 3번 틀릴경우 종료되니 주의해주세요." % self.match_count)
                self.PBE_Decrypt()
            else:
                print("alicePassword를 3번 틀리셨습니다. 시스템이 종료됩니다.")
                sys.exit()

        salt, encryptedCEK, iv, ciphertext = self.Read_USB()
        KEK = self.generateKEK(salt, alicePassword)  # input : salt, alicePassword  output : KEK
        decryptedCEK = self.aesDecForCEK(encryptedCEK, KEK, iv)
        plaintext = self.aesDecrypt(ciphertext, decryptedCEK, iv)
        print("AES Decrypted plaintext: %s" % plaintext)
        self.finishDec += 1
        print()
        return plaintext

def main():
    pbe = PBE()
    pbe.PBE_Encrypt()
    pbe.PBE_Decrypt()

if __name__ == "__main__":
    main()