#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

    cursor = conn_db.cursor()
    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
