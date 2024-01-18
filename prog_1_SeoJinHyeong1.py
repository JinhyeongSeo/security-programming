from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

# Alice의 공개키
alice_public_Key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyFzLS4Wb2M2RkqjsHym3\n10WEqA3hDoll9Yy8aZ7KZNMhOh31tQhwjglRr3sgsO4T9hlqPmY970fLn/p+yZUI\nbtfsGP3iHxpqflvTI2jp0MVIamKUDtY9mgsvjbIFaatzzROpnB7TP+ijCvm8sxAQ\n5RhLAm4Kk6bNVLom4GllRbI6gzcS+pZIC+A07plaK2DdLC01TQ07uH4942YyQnUF\nlSQF4STgHpCDp0I3PIQsUoBvPyXS48Jy+6sWiLlkFKfj4q85Sh+SMp8qpdvpHdQH\nrj2XQ1Cl+Zc9ZG5kzkfXDnE8WBgEmZFkHxQHNsHf7ppEV7IOBrxPONNhDayw3oQE\nGQIDAQAB\n-----END PUBLIC KEY-----'

# Bob의 개인키
bob_private_Key =b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA7ETnLxJS+12tVdinWR3LSyj2VFAhawjSkIi7dFaPSkhL746x\nX7s5lDqhX/5uRF83HGlt1YoiywLTWKYr7SRBETMqhq5CiEwZgYgx8tu6SAWX6HE7\nQrKSas5qKQ1+sdinr1OgdSuh2leh4l1WHiVoS64eNVZJuPhbrMKmPqx+t6PFqLJP\ncxSSsENALqLXhVFyk4w18mjurN/kVdn8bpxlXBksl6Y1cB4t4Rpx6F8f+DO19S7m\ng6SJPsT0vyHhkGGx1J088Y8yIByUfFgyuhWff+sirpgL9KuC0eQtuEG32ka4JAWK\nHtsotG0VblPMvicZmTgckiqifMiJxBZYzEfYSwIDAQABAoIBAAdv99MMgZ42CbHN\nGx98B507Ed3/k725zl8MXtI/s00ET5ef50d7LknTOqc57CCs2qBDVVjGe2fmk96T\nhIh3frDa6njI3YFK2/au4duiPQ/tVSXVAqeL1X4VN1RJf3Z7unOTb1ag4/xqi8cD\nZyWVyd2wAnVtXO68qq4ahn8skOSY7K80Hr5ax1Q5qE6MNBo2ROp1HgBFG29HaoH6\nurgfYTLznTw20XyW2V0MKmmCFt2BW9lskkyFNVbBXyoZsVoyrJDUADtJJoJTwlep\ni0RJDs10scd6OK9aoaEqEUsfL7+Gg/wu9aXNzsodyJFY0mxCgWmM1f+EyhS7vB01\nwLy+CHECgYEA7mh7d+ixHY1+XghlhQROqOJlILRvYNgefPNxws3YuMKV62/yftNT\nPWLsfQKuDyzuocqC8zk8WD5curVckIRwM55P62Dtfm+WMsFC5Dv2BCA3OrUUmKnD\nTU/f/QsWKpsGNIuec+oAmgm8TMdzyrWvjjLVAJlQO4CWIID1sZIQnDMCgYEA/bQD\n+J0vgK0CHk7gyzFsIBflYcIeUlfwNnGETp4lawnWnt19Jn35+dADlaK+i5IJOQx3\nHzUf3R7YakBDtZLzgf8in7TxZNUZOPoC8y7J+R98aIMBoYHXFiNfVx8Gtnsnwa2h\nDuoYKC1JlETrNGdn012rgqzvjCXKUVHJbHiJu4kCgYEAoV8Hc7qFaEOF7ZAxZz/r\nHlVfritz2FFxEZKWxg0fTLApWhuEQGQ6S6rR+CwANTVssQaqbIepWPGdQqPP6+I5\nMDdQUTpihtpxCBnYdTRA6boEqDA5qLv//iy6qEUA1AXqxVZcAom5roo4cp/uuJ8S\nHWY61xTvQddfxtCDfZYouBECgYEAvlQkfoj9sB0a773hKs8C/PiwXyyQLtpGHbH/\nvjMqgyi4WCp1z0DHHkCNz95t8Ks4PBI786+ZHfwcA2n+4eNCx42uXf4S8sBj0bjO\nKb46S6jxXj6aJJ4RzEvxJJzkHlY6NzSZFWVNhiajgpZJleDVpV4qYzh15cAcDfG7\nmKK9QXECgYBCQ/gCVsNNjRhWEqdsFpD3Tc9Q6HDU2KpOUeFUnpgtxXqL9LzQa/9p\n3TBb9p3237+VDBQPQKMIZ/zCQzVpM5pZLio/KVmoEP+fOwji6+EFd/wWRFkD7guK\nCk6VTH8zQFWaDPSQbFgdzqEAY8eS9Njnm89b59Tswtq8uWg3OhVcZA==\n-----END RSA PRIVATE KEY-----'

def rsaDecrypt(encrypted, priKey):
    privateKey = RSA.import_key(priKey)
    rsaCipher = PKCS1_OAEP.new(privateKey)
    plaintext = rsaCipher.decrypt(encrypted)
    return plaintext

def aesDecryptWithIV(encrypted, key):
    BLOCK_SIZE = 16
    iv = encrypted[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.decrypt(encrypted[BLOCK_SIZE:]).rstrip(b'\x00')  # 패딩 제거

# Alice의 최종 출력 (RSA로 암호화된 AES 키 + AES로 암호화된 SignMsg + Message)
Alice_Final_Output = b'_\x93\x1e2*\xc4\x13\x93\x1bM\x92\x1c\x01q\x8f>\x10\xa9 ou\xc7Zg\xbb\xf57\xab\xbd\xd2\x9aw\xd8f\xb4\xd4x\x97j\xc1\x17\x9dMEm\xd6\xa5\x04A 8Z9#\x81`{\x13\xfc\xd9\xe3\x08\xb0D\xcc\xb640\x8c\xd2S\x14\xd9\xa6\xc8M\x86\x043\x82 \xc6\xa76\xb7\xb0\x03i\x8a\xc4\x8e%+\xcdX\xa8>]\x0fb\xf5\xb8\xb1u|\x17\x83\xd7\xaf\x1b\xcb\xff\x96\x1d\xeb\xc3B1VU\x9e\xd1\x0c+.NR\xe0FR\x05}\x85\x8f\xa6\xb5\xc9\x82!\xc6u\xfd\xd3\xdeZtv\x8e\x10U?\x80G\x03\x94\x00\x1b\xc0\x1b\xdf^\xd7\xd0n$\xd4-\x1a\r\xcf\x07\x80T\xe1\xb8\xef\xcd\xcd\xfa\x1a\xac<Gc\xd1\xe8\x00\x12\xcdj\x87\xe3H\xd7\x8f#O\xad\x8a\xefYU\xcc\x8e\xa4g<z\xd7\xeeF5\x91\xc8\x04\xd6\xb8\xbbC\xf1\xd8F\x9a)\xf7{I\x14m\x03\xdb\xfb\xab\xaa\x0e\xbdu\x1d\xbf\x88\x06\xea\xf8\xde\x13\xd7\xd0\xcc|bU\x03\xaa\x0e\xf7$******$abcdefghijklmnop\xd1X\xc7\xff\x15\xe9\x08 \xc1\xae\xc2|R\xb5"Q\x9a\xb5+c\xd5T\x1a\x00kI\r8C\xa5\x12\xe0\xbd\xb2\x96\t\x90\xbe\xa1,X\xf3g\x9c`h\x8f\x8c,\xaa\x8e\xab\xe1\xfc\x90\x9e\xbf\xc59\xba\xfb\xa2\xfeL\xa0*\xb6b8/\xff\xfa\x8cZk\xe9\xe5vJ]\xf6\n\xa5\xe9\xd2"\xf7\xde\x0e\x1e\x15\xf4A@\xb1\x86\xed\x08>\x1e\xc8\x9a\x8c\xaf\xb9\xda\xf5>U\x86\xc9,b\xa9\xa5\xea\xf8&\xaa\xeb\x8a}\xb9\x98\xb6Yl:\xb2\xf0\xb4\xa0q\xf5\x0b\x9e\xf8\xb2\x03\xb1\xb8\x92\xd1O}+\x9d\x1eY\x8ata)\xf2!\xbc\xe0\xe6\xa9A\x05t)\xe5\x1bmfR\x0e\'\x00\xf9|\x9eO$:\x81\x03\xb0\x91\xec/\xd2\xdb\xf5\xee\x9fe{v\xe2\x02\xf2@\xa06\x05G\x0c.t\xef\x8b\xca\x89\xa2\xef\xb7\xb7\'0\xe6v\xf6\xc4\xa0\x9c\xe7\x91_n\x8bs\x9f=3\\P\xca\xed\xaa\xd4\x976|\x9aE\xef\xc4\xe5\xac\x85\x85\x9e\x05\xdaDz`\xb15\xe0\xd3\x16\x92p\x00\xf7\xbfp\x08\xbc\xben|}"\xe7KH\xb5>\xfc\x82\xc7\x94.a\x81\x0es\xd7\xc8\x95\xf9\x8c\x99\xd0\xac\xd6l\x02\x1e\xd3Bhp\xf0\xb2\x0f\'\x07\\\xd1\x81\xc6i\xcc\xbd\xb1\xd4\x87\x8a\xd6\xc6\x85\xf4\x8b`l\x0ciN\x10\x9d\xf2\x84\x1e\x8b\x9f\x8dZ\xc0\x16\x8b\xcd\xdf\xe0\xaa\xbaP!\xca\x1a\xbf}\xdb\xb4$#\x83\x06a0\x00Jrr$\xd7\xbf4\xf2\xa8\x972\x0fZ"'  # Alice의 최종 출력 값을 여기에 넣으세요

# RSA로 암호화된 AES 키와 AES로 암호화된 SignMsg와 Message를 분리
receiver_encryptedAESKey, receiver_encryptedSignMsgPlusMessage = Alice_Final_Output.split(b"$******$")

# RSA로 암호화된 AES 키를 Bob의 개인키로 복호화
decryptedKey = rsaDecrypt(receiver_encryptedAESKey, bob_private_Key)

# AES 키를 사용하여 AES로 암호화된 SignMsg와 Message를 복호화
decryptedSignMsgPlusMessage = aesDecryptWithIV(receiver_encryptedSignMsgPlusMessage, decryptedKey)
decryptedSignMsg, decryptedMessage = decryptedSignMsgPlusMessage.split(b"$******$")

print("Decrypted Message:", decryptedMessage.decode())
