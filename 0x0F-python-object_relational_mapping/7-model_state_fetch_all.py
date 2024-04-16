#!/usr/bin/python3
"""
A python file that contains the class definition
of a State and an instance Base = declarative_base()
"""


from sys import argv
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()

class State(Base):
    """Created a TABLE using ORM
    Object Relational Mapping
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"State(id={self.id}, name='{self.name}')"
