#!/usr/bin/python3
"""City model
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class, links to MySQL cities table
    """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)