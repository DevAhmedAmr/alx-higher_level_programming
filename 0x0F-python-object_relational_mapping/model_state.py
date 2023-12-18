#!/usr/bin/python3
"""doc0"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()
"""doc1"""

username = sys.argv[1]
password = sys.argv[2]
hostname = "localhost"  # or the address where your MySQL server is hosted
port = "3306"  # default MySQL port is 3306
database_name = sys.argv[3]

# MySQL connection string format: 'mysql://username:password@hostname:port/database_name'
connection_string = f"mysql://{username}:{password}@{hostname}:{port}/{database_name}"
engine = create_engine("sqlite:///:memory:", echo=True)

"""doc2"""


class State(Base):
    """doc3"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
