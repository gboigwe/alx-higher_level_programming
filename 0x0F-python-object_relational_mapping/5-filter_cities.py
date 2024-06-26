#!/usr/bin/python3
"""
Write a script that takes in
the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == '__main__':

    conn_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = conn_db.cursor()

    query_l = """SELECT cities.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""

    cursor.execute(query_l, (sys.argv[4],))

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    conn_db.close()
