from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models

class Movie(models.Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    description = Column(String(255),nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("directors.id"))
    director = relationship("Director")


class Genre(models.Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class Director(models.Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()




class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()

class User(models.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()


