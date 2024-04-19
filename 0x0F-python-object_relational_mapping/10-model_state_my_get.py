#!/usr/bin/python3
"""
Write a script that prints
the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3], pool_pre_ping=True))

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    session = Session()
    arg_forth = argv[4]
    search = session.query(State).filter(State.name == (arg_forth))

    try:
        print(search[0].id)
    except:
        print("Not Found")

    session.close
