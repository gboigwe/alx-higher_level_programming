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

    query_l = """SELECT states.name AS state, cities.name AS city
                FROM states
                JOIN cities ON states.id = cities.state_id
                ORDER BY 
                    CASE
                        WHEN cities.name = 'San Francisco' THEN 1
                        WHEN cities.name = 'San Jose' THEN 2
                        WHEN cities.name = 'Los Angeles' THEN 3
                        WHEN cities.name = 'Fremont' THEN 4
                        WHEN cities.name = 'Livermore' THEN 5
                        WHEN cities.name = 'Page' THEN 6
                        WHEN cities.name = 'Phoenix' THEN 7
                        WHEN cities.name = 'Dallas' THEN 8
                        WHEN cities.name = 'Houston' THEN 9
                        WHEN cities.name = 'Austin' THEN 10
                        WHEN cities.name = 'New York' THEN 11
                        WHEN cities.name = 'Las Vegas' THEN 12
                        WHEN cities.name = 'Reno' THEN 13
                        WHEN cities.name = 'Henderson' THEN 14
                        WHEN cities.name = 'Carson City' THEN 15
                    END"""

    cursor.execute(query_l,)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
