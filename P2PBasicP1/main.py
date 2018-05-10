# coding: utf-8
import socket;
import struct;
import sys;
import threading;

from Ethernet import Ethernet;
from ARP import ARP;

class Packet:
	def __init__(self, raw):
		self._raw = raw;
		self._eth = Ethernet(raw[:14]);
		self._arp = ARP(raw[14:]);

	@property
	def raw(self):
		return self._raw;

	@property
	def eth(self):
		return self._eth;

	@property
	def arp(self):
		return self._arp;

def recv_message(host_socket):	#client에게 받는 메세지를 처리하는 쓰레드
	while True:
		message = host_socket.recv(4096).decode();
		print('-->'+message[5:9]+'<--');
		print('\n'+message+'\n[P1] ', end='');
		if message[5:9].lower() =='quit':
			break;

	print('recv P2 Disconnected');

def send_message(host_socket):	#host가 client들에게 메시지를 보낼때 쓰는 쓰레드
	while True:
		message = input('[P1] ');
		host_socket.send(('[P1] ' + message).encode());

		if message[0:4].lower() =='quit':
			break;

	print('send P2 Disconnected');

def main():
	port_number = 12000;

	print('wait connection');
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	server_socket.bind(('',port_number));
	server_socket.listen(10);	# 10으로 설정해서 최대 connection을 10개 까지 만들수있다.

	countSocket = [];	#accept()에서 반환된 socket object를 저장하기위함.
	countAddr = [];	#accept()에서 반환된 address를 저장하기위함.
	sendThreads = [];
	recvThreads = [];

	while True:
		(host_socket, addr) = server_socket.accept();
		countSocket.append(host_socket);
		countAddr.append(addr);
		if(len(countSocket)>10):	#연결이 10개를 넘어가면 프로그램 종료
			print('Too Many');
			break;

		for sockets in countSocket:
			r1 = threading.Thread(target = recv_message, args = (sockets, ));
			s1 = threading.Thread(target = send_message, args = (sockets, ));
			r1.daemon = True;
			s1.daemon = True;
			r1.start();
			s1.start();

	for sockets in countSocket:
		sockets.close();
		print('end');

if __name__ == "__main__":
	raw = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003));
	raw.bind(('eth1',0));
	print('start sniff.');

	while True:
		data = raw.recv(65535);
		packet = Packet(data);
		if packet.eth.type == 0x0806:
			print(packet.eth.src, '->', packet.eth.dst, packet.eth.type);
			print('senderMac : ', packet.arp.senderMac);
			print('senderIP : ', packet.arp.senderIp);
			print('targetMac : ', packet.arp.targetMac);
			print('targetIP : ', packet.arp.targetIp);
