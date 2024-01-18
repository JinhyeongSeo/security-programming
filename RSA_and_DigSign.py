from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5

def gen_RSA_Key(userName):
    privateKey = RSA.generate(2048)
    priKey = privateKey.exportKey('PEM')
    print("%s private Key: %s" % (userName, priKey))
    pubKey = privateKey.publickey()
    print("%s public Key: %s" % (userName, pubKey.exportKey('PEM')))
    return priKey, pubKey


def rsaEncrypt(message, pubKey):
    rsaCipher = PKCS1_OAEP.new(pubKey)
    ciphertext = rsaCipher.encrypt(message)
    return ciphertext


def rsaDecrypt(encrypted, priKey):
    privateKey = RSA.importKey(priKey)
    rsaCipher = PKCS1_OAEP.new(privateKey)
    plaintext = rsaCipher.decrypt(encrypted)
    return plaintext


def rsaDigSignGen(message, priKey):
    hashMsgObj = SHA512.new(message)   #hashMsgObj = SHA512.new();  #hashMsgObj.update(message)
    privateKey = RSA.importKey(priKey)
    signGenObj = PKCS1_v1_5.new(privateKey)
    signMsg = signGenObj.sign(hashMsgObj)
    return signMsg


def rsaDigSignVerify(signMsg, message, pubKey):
    hashMsgObj = SHA512.new(message)
    signVerifyObj = PKCS1_v1_5.new(pubKey)
    if signVerifyObj.verify(hashMsgObj, signMsg):
        return True
    else:
        return False


def main():
    message = b'Information security and Python Programming, Test Message!!! Big Brother???'
    print("Message: ", message.decode())

    #alice & bob RSA key pairs Generation
    alice_priKey, alice_pubKey = gen_RSA_Key('alice')
    bob_priKey, bob_pubKey = gen_RSA_Key('bob')

    #alice --> bob : message encrypt ---> sending...
    #alice : using 'bob" publickey message encrypt
    encrypted = rsaEncrypt(message, bob_pubKey)
    print("RSA_Encrypt(message, bob_pubKey): ", encrypted.hex())
    #alice : message --> digital signature generation
    signMsg = rsaDigSignGen(message, alice_priKey)
    print("Digital Signature on input Message: ", signMsg.hex())
    print("Size of Digital Signature: ", len(signMsg))

    """
    Client-Server Network(TCP/IP) Data Sending :  "encrypted" data + "signMSG (digital signature)" data + "alice publicKey Certificate"
    """

    # Network : from alice (encrypted --> sending) to bob
    #bob : decrypt ... using bob's privateKey...
    #bob : "encrypted" data + "signMSG (digital signature)" data

    decrypted = rsaDecrypt(encrypted, bob_priKey)
    print("RSA_Decrypt(ciphertext, bob_priKey): ", decrypted.decode())
    ### alice 의 인증서 안에 있는 alice의 공개키 획득...
    if rsaDigSignVerify(signMsg, decrypted, alice_pubKey):
        print("Digital Signature on Decryption Message: Correct. Verification OK!!!")
    else:
        print("Digital Signature Verification Fail!!!")


if __name__ == "__main__":
    main()