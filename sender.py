#importing socket module
import socket
#                ipv4,         UDP type
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#what is my receiver address
recvr_addr=("127.0.0.1",9898) 
#Now i want to send messege
user_data= input("Enter your messsge:- ")
#converting data into ascii code
newdata=user_data.encode('ascii')
#now you can send data
s.sendto(newdata,recvr_addr)
print("your message has been send....")