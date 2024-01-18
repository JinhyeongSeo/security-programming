from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# creation 256 bit session key
sessionkey = Random.new().read(32) # 256 bit

# encryption AES of the message
f = open('./Hybrid/plaintext.txt','rb')   ### signature.txt || plaintext
plaintext = f.read(); f.close()
iv = Random.new().read(16) # 128 bit
obj = AES.new(sessionkey, AES.MODE_CFB, iv)
ciphertext = iv + obj.encrypt(plaintext)
f = open('./Hybrid/ciphertext.txt','wb')
f.write(bytes(ciphertext)); f.close()

# encryption RSA of the session key
publickey = RSA.importKey(open('./Hybrid/received_bobpublickey.txt','rb').read())
cipherrsa = PKCS1_OAEP.new(publickey)
sessionkey = cipherrsa.encrypt(sessionkey)
f = open('./Hybrid/sessionkey.txt','wb')
f.write(bytes(sessionkey)); f.close()