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
    'description': fields.String(required=True, max_length=255, example='Владелец ранчо'),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtubeн'),
    'year': fields.Integer(required=True, example=2018),
    'rating': fields.Integer(required=True, example=8.6),
    'genre_id': fields.Integer(required=True, example=17),
    'director_id': fields.Integer(required=True, example=1),
})
