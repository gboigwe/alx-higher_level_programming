#!/usr/bin/python3
"""
Write a Python file similar to
model_state.py named model_city.py
that contains the class definition
of a City.

City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """ Class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
