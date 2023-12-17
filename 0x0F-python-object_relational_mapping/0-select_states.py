#!/usr/bin/python3"
"""blank"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                          port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])

    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    con.close()
    