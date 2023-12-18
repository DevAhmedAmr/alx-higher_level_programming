#!/usr/bin/python3
# Defines a State model.
# Inherits from SQLAlchemy Base and links to the MySQL table states.
"""doc"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()


username = sys.argv[1]
password = sys.argv[2]
hostname = "localhost"  # or the address where your MySQL server is hosted
port = "3306"  # default MySQL port is 3306
database_name = sys.argv[3]

connection_string = f"mysql://{username}:{password}@{hostname}:{port}/{database_name}"
engine = create_engine(connection_string, echo=True)


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
