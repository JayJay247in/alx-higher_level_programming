#!/usr/bin/python3
"""Prints all City objects ordered by state id and city id
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()