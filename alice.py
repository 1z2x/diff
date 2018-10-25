import socket
from Crypto import Random
from Crypto.Cipher import AES

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
s.bind((host, 5000))
s.listen(1)
conn, addr = s.accept()
key = b'1234567890123456'
C = AES.new(key, AES.MODE_ECB)

while 1:
    encrypted_msg = conn.recv(1024)
    print("zaszyfrowana wiadomość " + str(encrypted_msg))
    msg = (C.decrypt(encrypted_msg)).decode('utf-8')
    if msg == '':
        break
    print("po odszyfrowaniu: " + msg.strip('0') + '\n')

conn.close()

