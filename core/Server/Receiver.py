import socket
import os

HOST = ''
PORT = 8050

BUFFER_SIZE = 1024
END_STRING = 'THE_END'

IMG_DIR = "data/temp"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
ctr = len(os.listdir(IMG_DIR))
while 1:
    conn, addr = sock.accept()
    print(addr, "connected.")

    with open(IMG_DIR + '{}.jpg'.format(ctr), 'wb+') as output:
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if data:
                output.write(data)
                if END_STRING in str(data):
                    break
    print("Image {} received.".format(ctr))
    conn.close()
    ctr += 1
