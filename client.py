#FOR MESSANGING USING PYTHON
import socket
import sys
import time
#<<<<<<< patch-2
#time libarary used to operate standard time.
#=======
#can be used turtle libaray in future.
#>>>>>>> main
s = socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))
print(" Connected to chat server")
while 1:
            incoming_message = s.recv(1024)
            incoming_message = incoming_message.decode()
            print(" Server : ", incoming_message)
            print("")
            message = input(str(">> "))
            message = message.encode()
            s.send(message)
            print("message has been sent...")
            print("")
