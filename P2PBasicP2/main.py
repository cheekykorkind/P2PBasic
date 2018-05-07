# coding: utf-8
import socket
import sys
import threading

def recv_message(client_socket):
	while True:
		message = client_socket.recv(4096).decode();
		print(message);
		if message[7:11].lower() =='quit':
			break;

	print('P1 Disconnected');

def main():
	ip_address = '192.168.33.10';
	port_number = 12000;

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	client_socket.connect((ip_address, port_number));
	print('P1 connected');

	threading.Thread(target = recv_message, args = (client_socket,)).start();

	while True:
		message = input('[P2] ');
		client_socket.send(('[P2] ' + message).encode());

		if message[0:4].lower() =='quit':
			break;

	print('P1 Disconnected');
	client_socket.close();

if __name__ == '__main__':
	main();
