import socket
import Functions as F

HOST = "192.168.2.112"
PORT = 8050
bufsize = 1024
END = bytes('THE_END', "UTF-8")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
counter = 0
while 1:
    conn, addr = sock.accept()
    print(addr, "connected...")

    with open('data\\temp{}.jpg'.format(counter), 'wb+') as output:
        while 1:
            data = conn.recv(bufsize)
            if data:
                output.write(data)
                if 'THE_END' in str(data):
                    print("Image received.")
                    break
    conn.close()
    counter += 1
