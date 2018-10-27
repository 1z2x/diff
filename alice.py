import socket
import _thread
from Crypto import Random
from Crypto.Cipher import AES

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
key = b'1234567890123456'
C = AES.new(key, AES.MODE_ECB)

_thread.start_new_thread(recive_message, ())
_thread.start_new_thread(send_message, ())

while 1:
	pass
conn.close()

