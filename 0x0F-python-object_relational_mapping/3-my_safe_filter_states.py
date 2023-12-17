#!/usr/bin/python3
"""blank"""
import MySQLdb
import sys
import re
if __name__ == "__main__":
    """blank"""
    def sanitize_input(input_string):
        sanitized_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
        return sanitized_string

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         password=password, database=database)
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM `states` WHERE BINARY `name` = '{}'""".format((state_name)))

    data = cur.fetchall()

    for row in data:
        print(row)
    cur.close()
    db.close()
