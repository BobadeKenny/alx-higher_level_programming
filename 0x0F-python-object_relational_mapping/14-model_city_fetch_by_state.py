#!/usr/bin/python3
"""lists all City objects from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City
if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           encoding='latin1')
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(
            instance.State.name, instance.City.id, instance.City.name))
