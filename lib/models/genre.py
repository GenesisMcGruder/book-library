from models.__init__ import CURSOR, CONN

class Genre:

all = {}

def __init__(self, genre, id=None):
    self.id = id
    self.genre = genre

def __repr__(self):
    return f'Genre: {self.genre}'

@property
def genre(self):
    self._genre = genre

@genre.setter
def genre(self, genre):
    if isinstance(genre, str) and 1<= len(genre) <=10:
        self._genre = genre
    else:
        raise ValueError("Genre must be a string and between 1 and 10 characters")

@classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY,
                genre TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS genres;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO genres (genre)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.genre,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, genre):
        user = cls(genre)
        user.save()
        return user

    def update(self):
        sql = """
            UPDATE genres
            SET genre = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.genre, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM genres
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_by_db(cls, row):
        user = cls.all.get(row[0])
        if genre:
            genre.genre = row[1]
        else:
            genre = cls(row[1])
            genre.id = row[0]
            cls.all[genre.id] = genre
        return genre

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM genres
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_by_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM genres
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_by_db(row) if row else None

    @classmethod
    def find_by_genre(cls,genre):
        sql = """
            SELECT *
            FROM genres
            WHERE genre = ?
        """
        row = CURSOR.execute(sql, (genre,)).fetchone()
        return cls.instance_by_db(row) if row else None

    


