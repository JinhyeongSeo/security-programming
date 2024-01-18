from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# creation of signature
f = open('./Hybrid/plaintext.txt','rb')
plaintext = f.read(); f.close()
privatekey = RSA.importKey(open('./Hybrid/aliceprivatekey.txt','rb').read())
myhash = SHA512.new(plaintext)
signature = PKCS1_v1_5.new(privatekey)
signature = signature.sign(myhash)

f = open('./Hybrid/signature.txt','wb')
f.write(bytes(signature)); f.close()