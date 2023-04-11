import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    username = Column(String(10), nullable=False) 
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)   
    gravity = Column(Integer)   
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)   
    capacity = Column(Integer)   
    name = Column(String(250), nullable=False)
    cost = Column(Integer)   
    max_speed = Column(Integer) 

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)   
    name = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet")
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship("Vehicle")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet")
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship("Vehicle")
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship("Character")
    

render_er(Base, 'diagram.png')
