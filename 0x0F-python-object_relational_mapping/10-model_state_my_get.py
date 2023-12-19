#!/usr/bin/python3

""" script prints the State object with the name passed as \
            argument from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    hostname = "localhost"
    port = "3306"
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    connection_string = (
        f"mysql://{username}:{password}@{hostname}:{port}/{database_name}"
    )
    engine = create_engine(connection_string, echo=False)

    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(State).filter(State.name == (state_name))

    if result is not None:
        for i in result:
            print(i.id)
    else:
        print("Not found")
