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
