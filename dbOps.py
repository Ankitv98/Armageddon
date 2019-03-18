import sqlite3

conn = sqlite3.connect("chiron")
crsr = conn.cursor()


def ExtractAndSaveUserInfo(stt):
    userID = 1
    print(stt)
    comm = "INSERT INTO userbasics VALUES (" + stt + ");"
    print(comm)
    crsr.execute(comm)
    conn.commit()
    return userID
