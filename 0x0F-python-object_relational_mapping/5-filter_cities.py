#!/usr/bin/python3
"""
Write a script that takes in
the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == '__main__':

    conn_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = conn_db.cursor()
    forth_arg = sys.argv[4]

    query_l = "SELECT c.id, c.name, s.name \
          FROM states s, cities c \
          WHERE c.state_id = s.id \
          ORDER BY c.id ASC"

    cursor.execute(query_l, (forth_arg,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
