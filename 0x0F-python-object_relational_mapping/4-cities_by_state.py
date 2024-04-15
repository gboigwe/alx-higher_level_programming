#!/usr/bin/python3
"""
Write a script that lists all cities
from the database hbtn_0e_4_usa
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

    cursor.execute("""SELECT state.id, city.id, state.name
                    FROM states state, cities city
                    WHERE city.state_id = state.id
                    ORDER BY city.id ASC""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
