#!/usr/bin/python3
"""
Write a script that changes
the name of a State object
from the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).filter_by(id=2)
    for i in stmt:
        i.name = "New Mexico"
    session.commit()
    session.close()
