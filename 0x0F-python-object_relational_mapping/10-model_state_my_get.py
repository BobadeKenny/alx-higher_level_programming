#!/usr/bin/python3
"""lists all State objects that contain the letter a"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           encoding='latin1')
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State.id).filter(State.name == argv[4]).first()
    if instance is None:
        print("Not found")
    else:
        print(instance[0])
