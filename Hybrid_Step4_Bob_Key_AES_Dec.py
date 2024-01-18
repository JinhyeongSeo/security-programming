from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# decryption session key
privatekey = RSA.importKey(open('./Hybrid/bobprivatekey.txt','rb').read())
cipherrsa = PKCS1_OAEP.new(privatekey)
f = open('./Hybrid/sessionkey.txt','rb')
sessionkey = f.read(); f.close()
sessionkey = cipherrsa.decrypt(sessionkey)

# decryption message
f = open('./Hybrid/ciphertext.txt','rb')
ciphertext = f.read(); f.close()
iv = ciphertext[:16]
obj = AES.new(sessionkey, AES.MODE_CFB, iv)
plaintext = obj.decrypt(ciphertext)
plaintext = plaintext[16:]
f = open('./Hybrid/plaintext_Bob.txt','wb')
f.write(bytes(plaintext)); f.close()