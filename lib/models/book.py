from models.__init__ import CURSOR, CONN

  all = {}
     def __init__(self, name, author, page_count, user_id, genre_id, id=None):
        self.id = id
        self.name = name
        self.author = author
        self.page_count = page_count
        self.user_id = user_id
        self.genre_id = genre_id

def __repr__(self):
    return (
        f'Book: {self.name}, {self.author}, {self.page_count}' +
        f'Genre: {self.genre}'
    )