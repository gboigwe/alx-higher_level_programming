#!/usr/bin/python3
"""
A python file that contains the class definition
of a State and an instance Base = declarative_base()
"""


from sys import argv
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1],
                argv[2],
                argv[3]), pool_pre_ping=True
        )

    class State(Base):
        """Created a TABLE using ORM
        Object Relational Mapping
        """

        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)

    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
