from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тейлор Шеридан'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Йеллоустоун'),
    'description': fields.String(required=True, max_length=255, example='Владелец ранчо украл гуся у соседа...'),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtubeн'),
    'year': fields.Integer(required=True, example=2018),
    'rating': fields.Float(required=True, example=8.6),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=25, example='hj@jkv'),
    'password': fields.String(required=True, max_length=25, example='fgh456'),
    'name': fields.String(required=True, max_length=25, example='Петя'),
    'surname': fields.String(required=True, max_length=25, example='Аистов'),
    'favourite_genre': fields.Nested(genre)
})
