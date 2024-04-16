#!/usr/bin/python3
"""
A python file that contains the class definition
of a State and an instance Base = declarative_base()
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1],
                argv[2],
                argv[3]), pool_pre_ping=True
        )

    # Base.metadata.create_all(engine)

    # Session = sessionmaker(bind=engine)
    # session = Session()

    # for state in session.query(State).order_by(State.id).all():
    #     print("{}: {}".format(state.id, state.name))
    # session.close()

    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).order_by(asc(State.id)).all()

    for i in stmt:
        print("{:d}: {:s}".format(i.id, i.name))
    session.close()
