#!/usr/bin/python3"
"""blank"""
from MySQLdb import _mysql
import sys
if __name__=="__main__":
	user=sys.argv[1]
	password=sys.argv[2]
	database=sys.argv[3]
	db=_mysql.connect(host="localhost",user=user,
					
					password=password,database=database,port=3306)

	db.query("""SELECT * FROM states ORDER BY states.id ASC;""")

	result=db.store_result()

	for row in result:
		print(row)