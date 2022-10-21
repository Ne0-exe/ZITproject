import sqlite3
from sqlite3 import Error
import sort

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_project(conn, project, sD):

    sql = ''' INSERT INTO projects(IPs, Counts, Rank) VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def main():
    sD = sort.sortDict
    database = r"ipdatabase.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        ranksDict = [5, 15, 100000000000000000000]
        for x, y in sD.items():
            if y < ranksDict[0]:
                project = (x, y, 'safe');
            if y < ranksDict[1]:
                project = (x, y, 'concerning');
            else:
                project = (x, y, 'dangerous');

if __name__ == '__main__':
    main()
