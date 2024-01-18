from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Hash import SHA512
from Crypto.Signature import PKCS1_v1_5

def rsaDecrypt(encrypted, priKey):
    privateKey = RSA.importKey(priKey)
    rsaCipher = PKCS1_OAEP.new(privateKey)
    plaintext = rsaCipher.decrypt(encrypted)
    return plaintext

def aesDecryptWithIV(encrypted, key):
    BLOCK_SIZE = 16
    iv = encrypted[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.decrypt(encrypted[BLOCK_SIZE:])

def rsaDigSignVerify(signMsg, message, pubKey):
    hashMsgObj = SHA512.new(message)
    signVerifyObj = PKCS1_v1_5.new(pubKey)
    if signVerifyObj.verify(hashMsgObj, signMsg):
        return True
    else:
        return False

Alice_Final_Output = b'\xa5\x06E\xb0\x9a\x9a\xe9}\xeb\x12M\x12k\xa2\x86m\xbb\xff\x85\x1a#\x03\xae\xad\xe4~\xafg\xb6\xc4\x85cs\xf6*\x91O\x89]\xc4\xd6^\x0e\x03f\xe5\xe7\xf5h )\xf3\xa2\xc0x\xb5m@\x08?\xa8\xab\xa6:C\xa3r\xaf\x8c/\xe1)\xc4\x1a>d\xc6\nh\xe1\x91\\9\x86JL\x973D_S\x94\xa6\xe7\xa1\x0f\xc7R\xae|\x15:\xcf2f\x9ao\xfeZ\xe4j\xd2|\xc4\n\xf7\xf3]9\xac\xf3b\xe4\x81`,\x82\x80c\x14\xad\xc1\xa8y\x81H\x8d\xb55\x92\xdft\xd6\x1f\xc2A3\xd0\xac\x14\xc02\t\xde2c\xb1\xd4]\x80\xa3u\x95\x8a<fc\xcf\x89\x00\x1e\x9b<\\\x05\xe2D\xf7\xee\x12\xa0\x17\xb4\xd9>\xba\xd6\xcfZUrC\xf3\xa2EQ\x17\x81\x9f\xb4\x93\xa4\xcc(M\xef>`\xd2\xad&Y\xecx\xb2\xca\xcd*,\x03\xeb \x9e~\xcb\x01`\xe9\xf2\xa5M\xdf\xae\x8a\x08\x90 \x08\x7f\xf7\x9c\x84\xa8\x8d\xf7\x07>t\xb6~J]\x9bfX\xdb$******$abcdefghijklmnop\xcfI5\x9aM Nv\x13\xaa\xfc\xd5\xc0\x80~/\xfbz\xb9nG\xb35\xfb,^`\x80\xe8`\t\x05x\x93\xae\xda\xe4\x88\xe2-0\x14\xc0\x82\xd4\xf5]\x11\x17-C\x17~j\x1f\x10\xceq/\\\xa9D\xb4\x1bAZ_9\xd2\xe7W\x1f\xf36L\x9e<\xab7\x8f\x1cY\xa9\x99O\xe3\x89@\x82\xe8\xa89\x93\xd0Y\xab\xee\xae\xbd\x15;0F=4\xac\r\x16\x96U2\xa28\xa4\xfe\xf6\xe1\xa1\x02S\xddv\xf7\x03\xe5c\x15\xf0\xd5\x02\x97\x04\x7f#\xa0~\xc1\x1bY}$\x89\x80\xb6v\xb1]\xce\x90\xde\xc4?\\.\xf3\x1c\xadI\xf6c\xa8\xf5. \xaf\x99o@\xe0\x03,8\xe9\xd0\xc8Vl4\x1e\xb3>\xba\xb9W\xa8\xf13\xd8 \x105\t\xc4\xf3\xbd2\x94\x1bK\xd1\x98\xb04_E\x91\x9bm\xf0+@\x02d}X\xc6p\x19\x05.\xc0\x82\x8f\xb09Zm\x99\x95\xa5\xd1\x8f<\xed\x9d\xfeH_\x87\xec!;a\xb2\xae\x14\xc6\xe7\x08\x1f\xe2\xa3WY\xeb\x00p\x00\xf7\xbfp\x08\xbc\xben|}"\xe7KH\xb5>\xfc\x82\xc7\x94.a\x81\x0es\xd7\xc8\x95\xf9\x8c\x99\xd0\xac\xd6l\x02\x1e\xd3Bhp\xf0\xb2\x0f\'\x07\\\xd1\x81\xc6i\xcc\xbd\xb1\xd4\x87\x8a\xd6\xc6\x85\xf4\x8b`l\x0ciN\x10\x9d\xf2\x84\x1e\x8b\x9f\x8dZ\xc0\x16\x8b\xcd\xdf\xe0\xaa\xbaP!\xca\x1a\xbf}\xdb\xb4$#\x83\x06a0\x00Jrr$\xd7\xbf4\xf2\xa8\x972\x0fZ'

bob_private_Key =  b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAtxWk3watC+9yyKq+WXaMBFw5g3Yw6wvgZi3LM8I4/36a0M24\nbeT3/rdwbN1pTo+DearigSoAaLSdmbYDeJSz5TzslfRkTpaRh72kxYACRRo9XCAc\n8XfFll3TqQBjvX0qh2etddS9G0v5spVUemVpuOgHtr+KepZqPijvtsHWdXVmDz3S\nKo+8dUlOia5njt9ae4zyy4CF6nuRXZlPeYtCMBgv1ga+uVYEhsheXqyb6mx1RUWc\nnlRg6Vwou/gQ2e2LTDM3JItOTA1KGwbVuwLRGqJKGtAFyPjdbod6kggEAXbea0lE\nRv9JNN9XpTXKMrJ/ld2N/GbH72JEQvS0Nd1EqwIDAQABAoIBAA+pNE83nPnWY7Uy\nldHFSDjfQrQyGgEhJPLYm/czd/iy9b9CubH80hHh0yYc0nM7530y1ulBlINgX9LU\nNPvNjI3hZkN1glcOnihEWqHiT09l7TXCMXeeTTKNmBtuwxlkaYznm3jm175MA3H5\nQB6wKhj9EBvbypat4yyqB8dUUWn+mYYwlQBLm9f9VVS4pZwzZQ1Hh3ZdlD//rdyN\nXRvdq5L6ygof6+/0RNh3RT8DU9oG7Al3/KlkYHlH3E6Gh4ERv/GmcR+iZnR3956p\nav7BR3O5OOYlOprAZzXv5g06G7xNp7xzWJmR5eBALHE3egydjgZCuwV84Ii6q2N7\ngphu0sECgYEAvwUBgluoNYDj3G6idH+ww9UBDsAdv0aBVWGi363Vs6lF7jAgD8Qa\nKXQCZ+fF17f9DsIYZKdTy/DfsLm8YMrkRg5fR2Ht+xUrFGNRrhQIj9otIrmP9IJS\nZMFycfBSBwnth6JrNUIlclSLpAtlZYG4rdqrvNWm7EgyxhwEPEua1bsCgYEA9V2d\nnaxagZWh8AxX6+WUo5a4PmAX20zxSlAFtFQ2ipHbEaheakhtOqm818OvMqUz2ZI+\nv4cqgkN0Fc+BpUzPUg4iuDpHj7obSZlWpK0VjaZaF20GrXPQHrMmkdmwdt/o3n9L\n+Q7Igwcj52nHHHHLB1nNNA10mbrzBsaivg9GZdECgYArX5adI/TI2VBkABcRPuFD\nRj1sPQFEKl05pubVxWIN3nTLhc/x5IRQP1BAiacpuVRToozpZfkoCLSyKyp0C/3T\nTnYh/kGMTp0ujvLABTqAd3jiNqJSUbkluasj5f6qLH3r21xehnt8P2hJwnCuoMrv\nZwSx5w10/1vQEhKAImaw+wKBgQDH7AJcEa4g/eHXrMcKv6Jv9IOk1zk5B6VnDnLH\nbwKNv7BG3/AmG2NctCbZi2k6E99+fKnB9wlM4Fc62jvhiwc17ayefWYHlvVa76To\nQttX8l5fzgbt13qRORnJJx2gjmq4t/IYOdJo6K15hfellpZ+I86OhhQmmmwgbkL2\nJ44NsQKBgDmywDSrImJoqh8ZsPM5P7D3g4z+E90A+kZS6iINDSB7kgsNRZVmRDD/\ndavuK6KK9PYVERFG3Y2RmI8q+Gmth8kUCymTYlTxCwp0Akf3/pHP3/Eq066OG2my\nrdNhDpL0M/a/GwT4/S+F6kDNaL+gIhV1d5XIsz5JiUOXviNcljkC\n-----END RSA PRIVATE KEY-----'


receiver_encryptedAESKey,  receiver_encryptedSignMsgPlusMessage = Alice_Final_Output.split(b"$******$")
decryptedKey = rsaDecrypt(receiver_encryptedAESKey, bob_private_Key)
decryptedSignMsgPlugMessage = aesDecryptWithIV(receiver_encryptedSignMsgPlusMessage, decryptedKey)
decryptedSignMsg, decryptedMessage  = decryptedSignMsgPlugMessage.split(b"$******$")

print("Received Message: ", decryptedMessage.decode())
