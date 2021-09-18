import socket
import os
import time
from time import sleep

server_ip = '127.0.0.1'
server_port = 12345
buffer_size = 1024
buffer_filename = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is Starting...", server_port)
sock.bind((server_ip, server_port))

while True:
    file_name, client_addr = sock.recvfrom(buffer_filename)
    print(client_addr, "Connection Established...")

    file_name = file_name.decode()
    file_name = os.path.basename(file_name)

    fd = open(file_name, 'rb')
    buff = fd.read(buffer_size)

    while(buff):
        sock.sendto(buff, client_addr)

        sleep(10/1000)

        buff = fd.read(buffer_size)
    
    fd.close()
    print(file_name, "Sent Successfully...")