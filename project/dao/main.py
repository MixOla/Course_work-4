from typing import Optional, List

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    # def get_all_order_by(self, filter:str, page: Optional[int] = None) -> List[T]:
    #     stmt: BaseQuery
    #     pass

class UsersDAO(BaseDAO[User]):
    __model__ = User
