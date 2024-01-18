from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP

rsa = RSA.generate(2048)
priKey = rsa.export_key('PEM')
print(priKey)
pubKeyObj = rsa.public_key()
print(pubKeyObj)
pubKey = pubKeyObj.export_key('PEM')
print(pubKey)


message = b"Hello World!!!"



rsaObj = PKCS1_OAEP.new(pubKeyObj)
encMSG = rsaObj.encrypt(message)
print(encMSG)

priKeyObj = RSA.importKey(priKey)
rsaObj2 = PKCS1_OAEP.new(priKeyObj)
output = rsaObj2.decrypt(encMSG)
print(output)