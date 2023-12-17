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
	var=db.query("""SHOW states FROM hbtn_0e_0_usa ORDER BY states.id ASC;""")
	for row in var:
		print(row)