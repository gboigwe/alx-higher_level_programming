#!/usr/bin/python3
"""
Write a script that lists all cities
from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':

    conn_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = conn_db.cursor()

    query_l = """SELECT state.id, city.id, state.name
                    FROM states state, cities city
                    WHERE city.state_id = state.id
                    ORDER BY city.id ASC"""

    cursor.execute(query_l,)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
