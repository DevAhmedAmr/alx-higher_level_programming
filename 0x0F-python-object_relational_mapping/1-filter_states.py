#!/usr/bin/python3
"""blank"""
import MySQLdb
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         password=password, database=database)
    cur = db.cursor()
    # "SELECT * FROM products WHERE prod_name LIKE '%A'"
    cur.execute(
        """SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id""")

    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
