#!/usr/bin/python3
"""
A python script that prints
the first State object
from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1],
                argv[2],
                argv[3]), pool_pre_ping=True
    )

    start = sessionmaker(bind=engine)
    start.configure(bind=engine)
    session = start()

    f_state = session.query(State).first()

    if f_state:
        print("{}: {}".format(f_state.id, f_state.name))
    else:
        print("Nothing")
    session.close()
