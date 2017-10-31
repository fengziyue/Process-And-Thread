from socket import *
import threading
import time
import os

x=0
lock=threading.Lock()

def compute(st):
	global x
	lock.acquire()
	xx=x
	lock.release()
	xx=xx*xx
	st+='sssssss'
	time.sleep(40)
	lock.acquire()
	x=xx
	lock.release()

sock=socket(AF_INET,SOCK_STREAM)
sock.bind(('127.0.0.1',8009))
sock.listen(5)

while 1:
	print('process id :')
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
	global x
	x=data
	th1=threading.Thread(target=compute,args=(st,))
	th2=threading.Thread(target=compute,args=(st,))
	th1.start()
	th2.start()
	th1.join()
	th2.join()
	data=x
	end=time.time()
	
	s=str(data)
	t=str(end-start)
	s='result='+s+'and time is '+t
	tcpClientSock.send(s.encode('utf8'))
tcpClientSock.close()
sock.close()