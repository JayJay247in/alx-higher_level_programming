#!/usr/bin/python3
""" Lists all cities of a passed state from database
hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = ("SELECT cities.name FROM cities JOIN states ON \
             state_id = states.id WHERE states.name = %s ORDER BY cities.id")

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    print(", ".join(row[0] for row in rows))

    cursor.close()
    db.close()