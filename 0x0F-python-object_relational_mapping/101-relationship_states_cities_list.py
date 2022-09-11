#!/usr/bin/python3
"""lists all City objects from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           encoding='latin1')
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(
            instance.id, instance.name))
        for i in instance.cities:
            print("\t{}: {}".format(i.id, i.name))
