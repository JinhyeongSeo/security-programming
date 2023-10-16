from Crypto.Cipher import AES
from Crypto import Random

def myFunction():
    pass


def main():
    myFunction()
    message = "hong gildong, 23, 010-2345-4567,dep. of com. eng."
    message_value_list = message.split(",")
    print(message_value_list)


    user_lifo = {
        "name" : "hong gildong",
        "age" : "23",
        "phoneNum" : "010-2345-4567",
        "dept." : "dep. of com. eng."
    }


    print(AES.key_size)
    key = Random.new().read(AES.key_size[2])
    print(key.hex())

    print(message)
    print(message.encode())
    iv = Random.new().read(AES.block_size)
    print(iv)
    aesCipher = AES.new(key, AES.MODE_OFB, iv)
    print(aesCipher.encrypt(message.encode()))

if __name__ == "__main__":
    main()