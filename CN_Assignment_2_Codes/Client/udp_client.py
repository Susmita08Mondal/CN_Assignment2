import socket
import os
import time

ip = '127.0.0.1'
port = 12345
buffer_size = 1024
addr = (ip, port) 

print("List of Books: \n 1) Anthem \n 2) Candide \n 3) Carmilla \n 4) Dracula \n 5) Leviathan \n 6) Test - 10KB")
file_number = int(input())

if(file_number == 1):
    file_name = "Anthem.txt"
elif(file_number == 2):
    file_name = "Candide.txt"
elif(file_number == 3):
    file_name = "Carmilla.txt"
elif(file_number == 4):
    file_name = "Dracula.txt"
elif(file_number == 5):
    file_name = "Leviathan.txt"
elif(file_number == 6):
    file_name = "Test.txt"
else:
    print("Wrong Input, Try Again...")

file = file_name.split('.')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    start = time.time()
    sock.sendto(f"{file_name}".encode(),addr)
    file_name = file[0]+"<Protocol=UDP>"+"+"+str(os.getpid())+"."+file[1]
    
    with open(file_name, 'wb') as f:
        print("Receiving...")
        while True:
            sock.settimeout(2)
            data, server = sock.recvfrom(buffer_size)

            if not data:
                break
            
            f.write(data)
    

except:
    end = time.time()
    print(f"Time Required to Download the File: {end - start - 2 } seconds")
    print("Downloaded Successfully...", file[0]+".txt")

    file_size = os.path.getsize(file_name)

    throughput = round((file_size*0.001)/(end - start), 3)               
    print("Throughput: ",throughput,"kB/s")
    
    sock.close()

finally:
    sock.close()