from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("directors.id"))
    director = relationship("Director")


# class MovieSchema(Schema):
#
#     title = fields.Str()
#     description = fields.Str()
#     trailer = fields.Str()
#     year = fields.Int()
#     rating = fields.Float()


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


# class GenreSchema(Schema):
#
#     name = fields.Str()


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


# class DirectorSchema(Schema):
#
#     name = fields.Str()


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")


# class UserSchema(Schema):
#
#     email = fields.Str()
#     password = fields.Str()
#     name = fields.Str()
#     surname = fields.Str()
