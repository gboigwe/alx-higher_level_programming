#!/usr/bin/python3
"""
Next, write a script
14-model_city_fetch_by_state.py
that prints all City objects from
the database hbtn_0e_14_usa:
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    state_q = session.query(State, City).join(City).order_by(City.id).all()
    for s_name, c_name in state_q:
        print("{:s}: ({:d}) {:s}".format(s_name.name, c_name.id, c_name.name))
    session.close()
