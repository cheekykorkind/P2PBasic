# coding: utf-8
import socket
import sys
import threading

def recv_message(host_socket):	#client에게 받는 메세지를 처리하는 쓰레드
	while True:
		message = host_socket.recv(4096).decode();
		print(message);
		if message[9:13].lower() =='quit':
			break;

	print('P2 Disconnected');

def send_message(host_socket):	#host가 client들에게 메시지를 보낼때 쓰는 쓰레드
	while True:
		message = input('[P1]');
		host_socket.send(('[P1]' + message).encode());

		if message[0:4].lower() =='quit':
			break;

	print('P2 Disconnected');

def main():
	port_number = 12000;

	print('wait connection');
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	server_socket.bind(('',port_number));
	server_socket.listen(10);	# 10으로 설정해서 최대 connection을 10개 까지 만들수있다.

	countSocket = [];	#accept()에서 반환된 socket object를 저장하기위함.
	countAddr = [];	#accept()에서 반환된 address를 저장하기위함.
	while True:
		(host_socket, addr) = server_socket.accept();
		countSocket.append(host_socket);
		countAddr.append(addr);
		if(len(countSocket)>10):	#연결이 10개를 넘어가면 프로그램 종료
			print('Too Many');
			break;

		for sockets in countSocket:
			threading.Thread(target = recv_message, args = (sockets, )).start();
			threading.Thread(target = send_message, args = (sockets, )).start();

	for sockets in countSocket:
		sockets.close();

if __name__ == "__main__":
	main();
