#!/usr/bin/python3
import socket
import _thread
import time
from struct import pack
from Crypto.Hash import SHA256
from struct import unpack
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import number

def key_exchange():
	p = 0
	while number.isPrime(p) == False:
		q = number.getPrime(512)
		p = 2*q + 1
	
	g = 2
	while pow(g, 2, p) == 1 or pow(g, q, p) == 1: 
		g = number.getPrime(4)
	conn.send(bytes(str(p), 'utf-8'))
	print('p = ' + str(p) + '\n')
	time.sleep(1)
	conn.send(bytes(str(g), 'utf-8'))
	print('g = ' + str(g) + '\n')
	a = number.getRandomRange(1, p)
	A = pow(g, a, p)
	conn.send(bytes(str(A), 'utf-8'))
	print('A = ' + str(A) + '\n')
	m = conn.recv(1024)
	B = int(m)
	return str(pow(B, a, p))

def recive_message():
	while 1:
	    encrypted_msg = conn.recv(1024)
	    print("zaszyfrowana wiadomość " + str(encrypted_msg))
	    msg = (C.decrypt(encrypted_msg)).decode('utf-8')
	    if msg == '':
	        break
	    print("po odszyfrowaniu: " + msg.strip('0') + '\n')

def send_message():
    while 1:
        message = input()
        encrypted_msg = C.encrypt(bytes(message, 'utf-8').zfill(((len(message) // 16)+ 1) * 16))
        print("wysyłam: " + str(encrypted_msg))
        conn.send(encrypted_msg)
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
s.bind((host, 5000))
s.listen(1)
conn, addr = s.accept()
secret = bytes(key_exchange(), 'utf-8')
key = bytes(SHA256.new(secret).hexdigest(), 'utf-8')[0:32]
print()
print(key)
C = AES.new(key, AES.MODE_ECB)

_thread.start_new_thread(recive_message, ())
_thread.start_new_thread(send_message, ())

while 1:
	pass
conn.close()

