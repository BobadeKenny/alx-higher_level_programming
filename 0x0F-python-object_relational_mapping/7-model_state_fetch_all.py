#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                       .format(argv[1], argv[2], argv[3]),
                       encoding='latin1')
Session = sessionmaker(bind=engine)
session = Session()
for instance in session.query(State).order_by(State.id):
    print("{}: {}".format(instance.id, instance.name))
