import sqlite3
import analyse
import sys

ipL = analyse.ipList
sortDict = {ipL[0]:1}
sortDict = {i:ipL.count(i) for i in ipL}
dang_ips = {}

with open('ips.txt', 'w') as sys.stdout:
    sD = sortDict
    database = r'C:\Users\macie\OneDrive\Pulpit\ProjektZIT\ipdatabase.db'
    # create a database connection
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS ip_db (
               IPs TEXT,
               Counts INTEGER,
               Rank TEXT)"""

    cursor.execute(command1)

    ranksL = [5, 30]
    f = open('dang_ips.txt', 'w')
    for x, y in sD.items():
        if y < ranksL[0]:
            cursor.execute("INSERT INTO ip_db (IPs, Counts , Rank) VALUES(?, ?, ?)", (x, y, 'safe'))
            conn.commit()
            continue
        if y < ranksL[1]:
            cursor.execute("INSERT INTO ip_db (IPs, Counts , Rank) VALUES(?, ?, ?)", (x, y, 'concerning'))
            conn.commit()
            continue
        else:
            cursor.execute("INSERT INTO ip_db (IPs, Counts , Rank) VALUES(?, ?, ?)", (x, y, 'dangerous'))
            dang_ips[x] = y
            conn.commit()

    for key, value in dang_ips.items():
        f.write('%s appeared %s times\n' % (key, value))

    sql = "SELECT * FROM ip_db ORDER BY Counts ASC"
    cursor.execute(sql)
    rows = cursor.fetchall()


    conn.close()


