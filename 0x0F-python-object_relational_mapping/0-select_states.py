#!/usr/bin/python3"
"""blank"""
import MySQLdb
from MySQLdb.constants import FIELD_TYPE
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=user,
                        password=password, database=database, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC;""")

    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()