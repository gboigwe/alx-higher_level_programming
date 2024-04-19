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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(
                               argv[1],
                               argv[2],
                               argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a_state = State(name='Louisiana')
    session.add(a_state)
    ins = session.query(State).filter_by(name='Louisiana').one()
    print(ins.id)
    session.commit()
