from PGP_All_Common import *

KEY_GEN_STATUS = False
alice_privatekey = './HybridAlice/aliceprivatekey.txt'
alice_publickey = './HybridAlice/alicepublickey.txt'
bob_publickey = './HybridAlice/received_bobpublickey.txt'
# 키 공유 프로세스 (tcp/ip 기반 공개키 공유 과정)
# 2인 1조로 실제 네트워크 테스트시
# Send_File 에 있는 'localhost' 주소 == 상대방의 IP 주소로 설정/변경해야 함
# Receive_File 에 있는 'localhost' 주소 == 본인의 IP 주소로 설정/변경 (반드시 실제 IP 주소)

print("PGP : Alice")
choice = int(input("Input (0) RSA Key Generation, (1) Send public key, (2) Receive public key, (3) Exit : "))

while True:
    if choice == 0:
        KEY_GEN_STATUS = True
        PGP_Generate_Key_File(alice_privatekey, alice_publickey)
    if choice == 1:
        PGP_Client_Send_File_byUDP('localhost', 6001, alice_publickey)
    if choice == 2:
        PGP_Server_Receive_File_byUDP('localhost', 7001, bob_publickey)
    if choice == 3:
        break
    if KEY_GEN_STATUS == False:
        choice = int(input("Input (0) RSA Key Generation, (1) Send public key, (2) Receive public key, (3) Exit : "))
    else:
        choice = int(input("Input (1) Send public key, (2) Receive public key, (3) Exit : "))
