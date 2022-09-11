#!/usr/bin/python3
""" the State object “Louisiana” to the database"""
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City
if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           encoding='latin1')
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = State(name="California", cities=[City(name="San Francisco")])
    session.add(obj)
    session.commit()
