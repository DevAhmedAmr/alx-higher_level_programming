#!/usr/bin/python3
# Lists all City objects from the database hbtn_0e_14_usa.
# Usage: ./14-model_city_fetch_by_state.py <mysql username> /
#                                          <mysql password> /
"""doc"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State

import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    hostname = "localhost"
    database_name = sys.argv[3]
    port = 3306
    connection_string = (
        f"mysql://{username}:{password}@{hostname}:{port}/{database_name}"
    )
    engine = create_engine(connection_string, echo=False)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    result = session.query(City).filter(City.state_id == State.id).order_by(City.id)
    for r in result:
        state_name = session.query(State).filter(State.id == (r.state_id)).first().name
        print(f"{state_name}: ({r.id}) {r.name}")
