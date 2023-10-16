import string

message = "hansine university computer engineering information security and programming 2023"

#사전 읽어 들여서, 위 메세지 내 단어의 매칭 비율 계산

#dictionary.txt 파일 읽기
f = open("./dictionary.txt","r")
English_dic = {}
read_dic = f.read().split()

message_list = message.split()
match_count = 0
for word in message_list:
    if word.upper() in read_dic:
        match_count += 1

f.close()
#매칭 비율 계산
print("wordPercentege: ",float(match_count/len(message_list)*100))

LETTERS = string.ascii_letters + " "

message_only_letters = ""
for char in message:
    if char in LETTERS:
        message_only_letters += char
print(message_only_letters)
print("letterPercentege: ",float(len(message_only_letters)/len(message)*100))