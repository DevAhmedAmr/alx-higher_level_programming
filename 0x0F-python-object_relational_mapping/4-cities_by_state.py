#!/usr/bin/python3
"""blank"""
import MySQLdb
import sys
import re
"""blank"""

if __name__ == "__main__":

    def sanitize_input(input_string):
        sanitized_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
        return sanitized_string
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         password=password, database=database)
    cur = db.cursor()
    # "SELECT * FROM products WHERE prod_name LIKE '%A'"
    query = "SELECT id, name ,state_id FROM  cities ORDER BY cities.id ASC"
    query = """SELECT cities.id, cities.name , states.name
				FROM cities
				ORDER BY cities.id ASC;"""
    cur.execute(query)

    data = cur.fetchall()

    for row in data:
        print(row)
    cur.close()
    db.close()
