from socket import socket, AF_INET, SOCK_DGRAM
maxsize = 4096
hostname = 'localhost'
PORT = 12350
ADDRESS = (hostname, PORT)

server_sock = socket(family=AF_INET, type=SOCK_DGRAM)

#sock = socket(AF_INET,SOCK_DGRAM)
#sock.bind(('',12350))

while True:
    data, addr = server_sock.recvfrom(maxsize)
    print("Data from Client : ", data.decode())
    print("Client Address : ",addr)
    resp = "UDP server sending data..."
    server_sock.sendto(resp.encode('utf-8'),addr)
    if (data == 'OK'.encode()):
        break

server_sock.close()