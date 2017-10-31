from socket import *

c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8009))


data='9'
c.send(data)
data=c.recv(1024)
print(data)

c.close()