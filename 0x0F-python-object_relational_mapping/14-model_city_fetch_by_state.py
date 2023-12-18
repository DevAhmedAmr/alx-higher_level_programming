#!/usr/bin/python3
""" prints all City objects from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State
import sys

""" prints all City objects from the database"""


if __name__ == "__main__":
    """prints all City objects from the database"""
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    hostname = "localhost"
    port = 3306
    connection_string = (
        f"mysql://{username}:{password}@{hostname}:{port}/{database_name}"
    )
    engine = create_engine(connection_string, echo=False)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    result = session.query(City).filter(City.state_id == State.id).\
        order_by(City.id)

    for r in result:
        state_name = session.query(State).\
            filter(State.id == (r.state_id)).first().name
        print(f"{state_name}: ({r.id}) {r.name}")
