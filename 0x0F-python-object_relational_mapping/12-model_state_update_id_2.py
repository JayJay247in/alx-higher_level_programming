#!/usr/bin/python3
"""Changes the name of the State with id=2
to New Mexico
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()
    session.close()