#!/usr/bin/python3
# Prints the first State object from the database hbtn_0e_6_usa.
# Usage: ./8-model_state_fetch_first.py <mysql username> /
#                                       <mysql password> /
#
"""doc"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    hostname = "localhost"  # or the address where your MySQL server is hosted
    port = "3306"  # default MySQL port is 3306
    database_name = sys.argv[3]

    connection_string = (
        f"mysql://{username}:{password}@{hostname}:{port}/{database_name}"
    )
    engine = create_engine(connection_string, echo=False)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()

    for i in session.query(State).order_by(State.id):
        print(f"{i.id}: {i.name}")
