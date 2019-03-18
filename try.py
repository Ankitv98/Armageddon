import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)

stt = ""

while stt != 'quit':
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    data = clientsocket.recv(1024)
    print(data.decode())
    clientsocket.send(b'Gotcha')
    clientsocket.close()

    stt = data.decode()
    print(stt)