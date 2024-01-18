from Crypto import Random
#from InfoSecModule import aesEncWithHash, aesDecWithHash, genRSAKeys, rsaEncrypt
from InfoSecModule import *
from InfoSecModule_selfsigned import  *

def aesEncDecWithHashTest():
    KEY_SIZE = 32
    BLOCK_SIZE = 16  # 128 bits
    plaintext, key, iv = inputPlaintextAndGenKey_IV(KEY_SIZE, BLOCK_SIZE)
    ## 암호화 과정
    tempOutput = aesEncWithHash(key, iv, plaintext)
    ## 복호화 과정
    aesDecWithHash(key, iv, tempOutput)


def rsaEncDecTest():
    plaintext = b"information security..."
    # alice_privateKey, alice_publicKey = genRSAKeys(2048, "Alice")
    bob_privateKey, bob_publicKey = genRSAKeys(2048, "Bob")
    # Alice....
    output = rsaEncrypt(plaintext, bob_publicKey)
    # Bob....
    output2 = rsaDecrypt(output, bob_privateKey)

    alice_privateKey = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAnoH77K4zEBCd8VCUmkAhUhg0p+X4KPnI20XcsBdYnth1DdRu\ntJjRlVXO+S7YDJL6U5Tw9jPhroJOEYftApR6lBgmqt2wI1dTr3Qf6m9yqj9IUh8h\nMDTl5IZ9s3flcq9J/sS2BDG39PeUNE2LfI7Sd6l6ZG5OzXKBU//KP4vQmtAKCKPy\nJM1h5X1AFQergRV89bCIVDT7tJZEXT3aQrT99gw1VURGCxqnh03X7tWW/UiMmRRX\nexYthrGSTIvCjcJJErfzJpvGgIHd5O1XBA7N+Hz92rnZ2jVxfagkpxO8SrKdUjru\nNiVbkzch6UDhUBvFk+1pWKMZzcykD5IBbEsfPwIDAQABAoIBAApxigW4HIksbxud\nMY1QOGHOUnnVfxpECuXXnojDoQUmQeAdZQXlI7nxI2frnDSH4pJrN80g8fergjVJ\nfWY0Hjdvt+x+GsLZWBwxTIEHwshQzxUKFAe3FIaQDewrNCTwQ7HTiCKSnAo53bvs\neApG5rsXoYbIdcy3hKniKpMxRRdODy4IH+S9qMcFVVjj1rG3egmSB2O3SQrp6v4v\nwdmT9fcnVIZEwUZkt7ilXyHfttzKW970PuUPl+sL/Ccl/DQjPnECQ/D2alOmMrvK\nHvI2w3PqhnDTpjp1y7Vya7XudvHuEacwFEzx3Us+zbBFa3XZUGMdNTIvYU45x6Mx\nr36xliECgYEAxPo3IZrxsxi4Q7qRbyg7ESEAtbudVPocsDtXvlt6s9w9rw++bZ3T\nexfs7Lr+rzokTCXxek0tIxXnM3bv/itZoaQZAy/sKjqxmgJ2NjHi2r2HPuoofFZg\nzr1TDaOmxImQ0X7428KY587p6TeidJDXLw50ymA08uH5wGt76zj8MCkCgYEAzgDU\nkh4Z9mC+FjBqo+NWOffH1gzBG2SSIP3O3c9n2UV7x4K/2tlMgKjwwu6pNf2k+7fI\nhR7SkoZgactnKLCzM87cTVOgW0poIpD0aqwgd9+o454JD9fHds4yoo2r/zN+yE/l\nBbQK9LV5ZNuljhwQo4oAQCXPSzpfpNueZ8GmoScCgYAXNMdT/TYmfG4RBKTnrJyw\n2uuDfZP+k+zXUlZ3Bb4B/JuDyV4M+gAVS29NQIaKzFXEZt/5IaiErqrrZELH9gF8\nSqHrvzSakQmldE7K+buZO6T4Y4vbgi2rjaCARdx64R4foE7fTSDIhpcGM9i+1OWV\nFKXrxcPXLYpIAiG6R59maQKBgQDN3jqRA5ACjk+osR4BRnGnYJ3OpdRd4bW/TqXr\nORiZIz099sZwmPRBJ5Pj2sozcJXuEI5Nqq3ZTH0RfPpMyblsru+uP0JjuQo0cRQx\nfm68HUIUppx7vrJRYmNr25TlZrruyBkiB/li7/CvAGqEiDuAk6sIcECm92EZyXiW\nTAqPxQKBgHWod8Vu+Rbfw0uIS3njSQfIItlC53jWrf9BRb21cEaaIwGJN50TJIWR\nG2mn7t0soFzb9dSZKbdx8mDO0Ng6JUmUQ4lSnsoURdmP+oFrsnTmZOzlbi+rSn49\nKMlaBLlhMJH1wdGuh4zWft7daaKWg56+e0zr0x7Sy4gzZim/QFyu\n-----END RSA PRIVATE KEY-----'
    alice_publicKey = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnoH77K4zEBCd8VCUmkAh\nUhg0p+X4KPnI20XcsBdYnth1DdRutJjRlVXO+S7YDJL6U5Tw9jPhroJOEYftApR6\nlBgmqt2wI1dTr3Qf6m9yqj9IUh8hMDTl5IZ9s3flcq9J/sS2BDG39PeUNE2LfI7S\nd6l6ZG5OzXKBU//KP4vQmtAKCKPyJM1h5X1AFQergRV89bCIVDT7tJZEXT3aQrT9\n9gw1VURGCxqnh03X7tWW/UiMmRRXexYthrGSTIvCjcJJErfzJpvGgIHd5O1XBA7N\n+Hz92rnZ2jVxfagkpxO8SrKdUjruNiVbkzch6UDhUBvFk+1pWKMZzcykD5IBbEsf\nPwIDAQAB\n-----END PUBLIC KEY-----'
    # Bob ...
    output3 = rsaEncrypt(plaintext, alice_publicKey)
    # Alice
    output4 = rsaDecrypt(output3, alice_privateKey)


def aesHMACTest():
    #### HMAC Test
    KEY_SIZE = 32
    BLOCK_SIZE = 16  # 128 bits
    plaintext, key, iv = inputPlaintextAndGenKey_IV(KEY_SIZE, BLOCK_SIZE)
    hmacKey = input("Input MAC Key: ")
    hmacKey = hmacKey.encode()
    hmacData = generateHMAC(hmacKey, plaintext)
    print("HMAC length(Bytes): ", len(hmacData))
    plaintext_and_HMAC = hmacData + plaintext
    output = aesEncrypt(key, iv, plaintext_and_HMAC)

    # Verify HMAC
    received = output
    decrypted = aesDecrypt(key, iv, received)
    decrypted_HMAC = decrypted[:len(hmacData)]
    decrypted_plaintext = decrypted[len(hmacData):]
    hmacKey2 = input("Input MAC Key: ")
    hmacKey2 = hmacKey2.encode()

    if (verifyHMAC(hmacKey2, decrypted_plaintext, decrypted_HMAC)):
        print("Received Plaintext: ", decrypted_plaintext.decode())
    else:
        print("HMAC Error!!!")


def writeToCertFile(filename, cert_pem):
    with open(filename, "wb") as file_pointer:
        file_pointer.write(cert_pem)
        file_pointer.close()


def readFromCertFile(filename):
    with open(filename, "rb") as file_pointer:
        cert = file_pointer.read()
        file_pointer.close()
    return cert


def genCertificateToFile(hostname, certFilename, privatekeyFilename):
    cert_pem, key_pem = generate_selfsigned_cert(hostname)
    print(cert_pem)  # Certificate (X.509 포맷으로 생성, 내부에 공개키 저장되어 있음)
    print(key_pem)  # private Key
    writeToCertFile(certFilename, cert_pem)
    cert = readFromCertFile(certFilename)
    print(cert)
    writeToCertFile(privatekeyFilename, key_pem)
    privateKey = readFromCertFile(privatekeyFilename)
    print(privateKey)


def rasEncDecUsingCertificate(certFilename, privateKeyFilename, plaintext):
    myPublicKey = read_pub_key_from_cert(certFilename)
    print(myPublicKey)
    rsaCipher = rsaEncrypt(plaintext, myPublicKey.encode())
    print(rsaCipher)

    myPrivateKey = readFromCertFile(privateKeyFilename)
    rsaPlaintext = rsaDecrypt(rsaCipher, myPrivateKey)
    print(rsaPlaintext.decode())


def main():
    # AES 암복호화 과정 테스트
    aesEncDecWithHashTest()

    ## AES + HMAC 적용 압복호화 테스트
    aesHMACTest()

    ## RSA 암복호화 과정 테스트
    rsaEncDecTest()

    ## 인증서 생성 및 인증서를 이용한 RSA 암/복호화 과정
    hostname = "www.hs.ac.kr"
    myCertFile = "myCert.crt"
    myPrivateKeyFile = "myPrivate.key"
    plaintext = input("Input Plaintext: ").encode()
    genCertificateToFile(hostname, myCertFile, myPrivateKeyFile)
    rasEncDecUsingCertificate(myCertFile, myPrivateKeyFile, plaintext)    # hostname, certFilename, plaintext


if __name__ == "__main__":
    main()