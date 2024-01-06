#!/usr/bin/python3
# Changes the name of the State object with id = 2 to
# New Mexico in the database hbtn_0e_6_usa.
# Usage: ./12-model_state_update_id_2.py <mysql username> /
#                                        <mysql password> /
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

    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()
