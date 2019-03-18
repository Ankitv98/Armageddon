from Libb import *

import Algorithmia

def CardCreator():
    client = Algorithmia.client('simwMUzTtxRs30OR13kELwpYPnM1')
    algo = client.algo('nlp/Summarizer/0.1.7')
    userQueue = Queue()

    op = input("Tell Mode: ")
    if(op == '1'):
        while 1:
            tit = input("Input Title: ")
            dat = input("Enter Data: ")
            uid = int(input("Enter UserID: "))
            op = input("Enter mode (1 = summary, 2 = raw): ")
            if op == '1':
                dat = algo.pipe(dat).result
            userQueue.loadQueue(str(uid) + '.chr')
            userQueue.enqueue([tit, dat])
            userQueue.saveQueue(str(uid))

    else:
        while 1:
            # tit =
            # dat =
            print("Not available yet")
