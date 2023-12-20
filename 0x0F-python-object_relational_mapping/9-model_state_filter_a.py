#!/usr/bin/python3
"""Lists all State objects containing the letter a
"""
import sys
from model_state import Base, State

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
    states = session.query(State).order_by(State.id).filter(State.name.ilike('%a%')).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()