#!/usr/bin/python3
"""
Write a script that lists all
State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3], pool_pre_ping=True))

    session = Session(engine)

    for state in session.query(State).filter(State.name.like("%a%")):
        print(state.id, state.name, sep=": ")
    session.close()
