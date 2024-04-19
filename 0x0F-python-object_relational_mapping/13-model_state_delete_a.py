#!/usr/bin/python3
"""
Write a script that deletes
all State objects with a name
containing the letter a from
the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    fil_state = session.query(State).filter(State.name.like("%a%"))
    data = fil_state.all()
    for i in data:
        session.delete(i)
    session.commit()
    session.close()
