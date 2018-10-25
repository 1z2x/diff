import socket
from Crypto import Random
from Crypto.Cipher import AES

s = socket.socket()
host = '127.0.0.1'
port = 5000
key = b'1234567890123456'
C = AES.new(key, AES.MODE_ECB)

s.connect((host, port))

while 1:
    msg = input("wpisz wiadomość ->")
    encrypted_msg = C.encrypt(bytes(msg, 'utf-8').zfill(((len(msg) // 16)+ 1) * 16))
    print("wysyłam: " + str(encrypted_msg))
    s.send(encrypted_msg)
