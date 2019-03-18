import json
import socket  

from Libb import *

def CardSender():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 9999
    # bind to the port
    serversocket.bind((host, port))
    # queue up to 5 requests
    serversocket.listen(5)

    stt = ""

    userQueue = Queue()


    while stt != 'quit':
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))
        data = clientsocket.recv(1024)
        print(data.decode())
        # This is the userid! + number of cards required 
        ss = data.decode()
        aa = ss.split('.')
        # Get Userid and use it to get their queue
        ncc = int(aa[1])

        userQueue = userQueue.loadQueue(aa[0] + '.chr')

        for i in range(0, ncc):
            [ttt, dat] = userQueue.dequeue()
            print(ttt, dat)
            clientsocket.send(b'Gotcha')
        clientsocket.close()

        stt = data.decode()
        print(stt)

        # Now we need to convert this json to objects and store in database

