#!/usr/bin/python3
"""blank"""
import MySQLdb
import sys
import re
"""blank"""


def print_formatted(data: tuple):
    """prints the elements of a nested iterables formatted
        example: data = [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
                output: 1, 2, 3, 4, 5, 6, 7, 8, 9 """

    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end="")

            if i < len(data)-1:
                print(", ", end="")
            else:
                if j < len(data[i])-1:
                    print(", ", end="")
    print("")


if __name__ == "__main__":

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

    query = """SELECT cities.name
                FROM cities ,states
                where  states.name=%s And cities.state_id = states.id
                ORDER BY cities.id ASC;"""
    cur.execute(query, (state_name,))

    data = cur.fetchall()
    print_formatted(data)
    cur.close()
    db.close()
