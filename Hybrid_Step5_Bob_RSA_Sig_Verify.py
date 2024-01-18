from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# decryption signature
f = open('./Hybrid/signature.txt','rb')
signature = f.read(); f.close()

# signature verification
f = open('./Hybrid/plaintext_Bob.txt','rb')
plaintext = f.read(); f.close()
publickey = RSA.importKey(open('./Hybrid/received_alicepublickey.txt','rb').read())
myhash = SHA512.new(plaintext)

try:
    pkcs1_15.new(publickey).verify(myhash, signature)
    print("Signature Verification Result : True")
except (ValueError, TypeError):
    print("Signature Verification Result : False")