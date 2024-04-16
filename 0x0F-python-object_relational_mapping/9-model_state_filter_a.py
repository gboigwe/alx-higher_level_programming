#!/usr/bin/python3
"""
Write a script that lists all
State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import create_engine
