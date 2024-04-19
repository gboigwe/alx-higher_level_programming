#!/usr/bin/python3
"""
Write a script that adds
the State object “Louisiana”
to the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    newState = State(name="Louisiana")

    session.add(newState)
    session.commit()
    
    print(newState.id)

    session.close()
