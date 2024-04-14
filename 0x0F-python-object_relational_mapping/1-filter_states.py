#!/usr/bin/python3
"""
A script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':

    conn_db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host='localhost',
        port=3306
        )

    cursor = conn_db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()