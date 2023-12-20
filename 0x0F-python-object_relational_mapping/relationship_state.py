#!/usr/bin/python3
"""State model with relationship to City
"""
from relationship_city import Base, City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(Base):
    """State class linked to MySQL states.
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete", backref="state")