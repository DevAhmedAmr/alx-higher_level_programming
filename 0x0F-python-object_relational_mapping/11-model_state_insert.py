#!/usr/bin/python3
# Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
# Usage: ./11-model_state_insert.py <mysql username> /
#                                   <mysql password> /
#
"""doc"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    hostname = "localhost"
    port = "3306"
    database_name = sys.argv[3]

    connection_string = (
        f"mysql://{username}:{password}@{hostname}:{port}/{database_name}"
    )
    engine = create_engine(connection_string, echo=False)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_entry = State(name="Louisiana")

    session.add(new_entry)
    session.commit()
    print(new_entry.id)
