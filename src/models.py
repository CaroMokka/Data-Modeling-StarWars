import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name_user = Column(String(80), nullable=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)

class Character(Base):
    __tablename__ = 'character'  
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    birth_date = Column(String(80))
    height = Column(Integer)
    gender = Column(String(80))
    homeworld = Column(String(80))


class Favs_Character(Base):
    __tablename__ = 'favs_character'
    id = Column(Integer, primary_key=True)
    name_user = Column(String(80), ForeignKey('user.id'))
    id_character = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'    
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    diameter = Column(Integer)
    climate = Column(String(80), nullable=False)
    terrain = Column(String(80), nullable=False)
    population = Column(Integer)

class Favs_Planet(Base):
    __tablename__ = 'favs_planet'
    id = Column(Integer, primary_key=True)
    name_user = Column(String(80), ForeignKey('user.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    model = Column(String(80))
    manufacturer = Column(String(80))
    passengers = Column(Integer)
    

class Favs_Starship(Base):
    __tablename__ = 'favs_starship'
    id = Column(Integer, primary_key=True)
    name_user = Column(String(80), ForeignKey('user.id'))
    id_starship = Column(Integer, ForeignKey('starship.id'))
    user = relationship(User)





    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')