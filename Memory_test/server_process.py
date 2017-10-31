from multiprocessing import Process,Queue
from socket import *
import time
import os

def compute(q,st):
	x=q.get()
	st+='s'
	x=x*x
	print('process id :')
	print(os.getpid())
	time.sleep(40)
	q.put(x)

sock=socket(AF_INET,SOCK_STREAM)
sock.bind(('127.0.0.1',8009))
sock.listen(5)

while 1:
	print(os.getpid())
	print('waiting for connection')
	tcpClientSock,addr = sock.accept()
	print('connect from ',addr)
	data=tcpClientSock.recv(1024)
	data=int(data)
	st='sssssss'
	for i in range(100000):
		st=st+'sssssss'
	start=time.time()
	q=Queue()
	q.put(data)
	q.put(data)
	p1=Process(target=compute,args=(q,st,))
	p2=Process(target=compute,args=(q,st,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	data=q.get()
	end=time.time()

	s=str(data)
	t=str(end-start)
	s='result='+s+'and time is '+t
	tcpClientSock.send(s.encode('utf8'))
tcpClientSock.close()
sock.close()
