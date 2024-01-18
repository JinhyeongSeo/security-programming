from socket import socket, AF_INET,SOCK_DGRAM
MAX_SIZE = 4096
PORT = 12350
hostname = 'localhost'
ADDRESS = (hostname, PORT)

if __name__ == '__main__':
    client_sock = socket(family=AF_INET, type=SOCK_DGRAM)
    msg = "Hello UDP server"
    client_sock.sendto(msg.encode('utf-8'), ('',PORT))
    data, addr = client_sock.recvfrom(MAX_SIZE)
    print("Server says:")
    print(repr(data))