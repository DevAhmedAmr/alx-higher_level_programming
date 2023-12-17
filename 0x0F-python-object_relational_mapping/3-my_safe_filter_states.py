#!/usr/bin/python3
"""blank"""
import MySQLdb
import sys

if __name__ == "__main__":
    """blank"""
    def remove_special_characters(string):
        """blank"""
        special_characters = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
        new_str = ''
        for char in string:
            if char not in special_characters:
                new_str += char
        return new_str

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         password=password, database=database)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    data = cur.fetchall()

    for row in data:
        print(row)
    cur.close()
    db.close()
