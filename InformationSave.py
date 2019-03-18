import json
import socket
from dbOps import *
from Libb import *

def InfoSave():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 9998
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

        # Now we need to convert this json to objects and store in database

        userID = ExtractAndSaveUserInfo(stt)
        # Create a blank queue for him/her
        uq = Queue()
        uq.saveQueue(str(userID) + '.chr')