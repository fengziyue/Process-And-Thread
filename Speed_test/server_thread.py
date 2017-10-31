from socket import *
import threading
import time

x=0

def compute():
	global x
	x=x*x
	for i in range(10):
		x=x+i
		x=x-i
	print('compute done')

sock=socket(AF_INET,SOCK_STREAM)
sock.bind(('127.0.0.1',8007))
sock.listen(5)

while 1:
	print('waiting for connection')
	tcpClientSock,addr = sock.accept()
	print('connect from ',addr)
	data=tcpClientSock.recv(1024)
	data=int(data)
	print(data)

	start=time.time()
	global x
	x=data
	th=threading.Thread(target=compute)
	th.start()
	th.join()
	data=x
	end=time.time()

	s=str(data)
	t=str(end-start)
	s='result='+s+'and time is '+t
	tcpClientSock.send(s.encode('utf8'))
tcpClientSock.close()
sock.close()

