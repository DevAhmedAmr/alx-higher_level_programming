#!/usr/bin/python3
"""blank"""
from MySQLdb import _mysql
from MySQLdb.constants import FIELD_TYPE
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    my_conv = {FIELD_TYPE.LONG: int, FIELD_TYPE.CHAR: str}
    db = _mysql.connect(host="localhost", user=user,
                        password=password, database=database, port=3306,
                        conv=my_conv)

    db.query("""SELECT * FROM states ORDER BY states.id ASC;""")

    result = db.use_result()
    data = result.fetch_row(maxrows=0)
    for row in data:
        state_id = row[0]
        state_name_bytes = row[1]
        state_name = state_name_bytes.decode('utf-8')
        print((state_id, state_name))
