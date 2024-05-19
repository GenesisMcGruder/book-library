from models.__init__ import CURSOR, CONN
from models.user import User
from models.genre import Genre

class Genre:
    all = {}
     def __init__(self, name, author, page_count, user_id, genre_id, id=None):
        self.id = id
        self.name = name
        self.author = author
        self.page_count = page_count
        self.user_id = user_id
        self.genre_id = genre_id