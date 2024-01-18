import random
import string

def randomString(stringLength):
    letters = string.ascii_letters
    random_string = "".join(random.choice(letters) for i in range(stringLength))
    return random_string

stringLength = int(input("원하는 랜덤 문자열의 길이를 입력하세요: "))

random_password = randomString(stringLength)
print("Random String (stringLength : %d) is %s " %(stringLength,random_password))


