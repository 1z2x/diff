import socket
import _thread
from Crypto import Random
from Crypto.Cipher import AES

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
key = b'1234567890123456'
C = AES.new(key, AES.MODE_ECB)

s.connect((host, port))

_thread.start_new_thread(recive_message, ())
_thread.start_new_thread(send_message, ())

while 1:
    pass

