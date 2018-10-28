import socket
import _thread
from struct import pack
from struct import unpack
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Util import number
from Crypto.Cipher import AES

def key_exchange():
	m = s.recv(1024)
	p = int(m)
	print(p)
	print()
	m = s.recv(3)
	g = int(m)
	print(g)
	print()
	b = number.getRandomRange(1, p)
	B = pow(g, b, p)
	m = s.recv(1024)
	A = int(m)
	s.send(bytes(str(B), 'utf-8'))
	print()
	return str(pow(A, b, p))
	
def recive_message():
	while 1:
	    encrypted_msg = s.recv(1024)
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
        s.send(encrypted_msg)

s = socket.socket()
host = '127.0.0.1'
port = 5000
s.connect((host, port))

secret = bytes(key_exchange(), 'utf-8')
key = bytes(SHA256.new(secret).hexdigest(), 'utf-8')[0:32]
C = AES.new(key, AES.MODE_ECB)



print()
print(key)

_thread.start_new_thread(recive_message, ())
_thread.start_new_thread(send_message, ())

while 1:
    pass

