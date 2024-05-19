from models.__init__ import CURSOR, CONN
from user import User
from models.genre import Genre

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
@property
def name(self):
    return self._name

@name.setter
def name(self.name):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern, name):
        self._password = password
    else:
        raise ValueError("Name must be an alphanumeric character")

@property
def author(self):
    return self._author

@author.setter
def author(self, author):
    if isinstance(author, str):
        self._author
    else:
        raise ValueError("Author must be a string")

    
@property
def page_count(self):
    return self._page_count

@page_count.setter
def page_count(self, page_count):
    if isinstance(page_count, int) and 1<= len(page_count) <=8:
        self._page_count = page_count
    else:
        raise ValueError("Page count must be a number and between 1 and 8")

@property
def user_id(self):
    self._user_id

@user_id.setter
def user_id(self, user_id):
    if type(user_id) is int and User.find_by_id(user_id):
        self._user_id = user_id
    else:
        raise ValueError("Must be user reference")

@property
def genre_id(self):
    self._genre_id = genre_id

@genre_id.setter
def genre_id(self, genre_id):
    if type(genre_id) is int and Genre.find_by_id(genre_id):
        self._genre_id = genre_id
    else:
        raise ValueError("Must be a genre reference")


@classmethod
def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                name TEXT,
                author VARCHAR(100),
                page_count INTEGER,
                user_id INTEGER,
                genre_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

@classmethod
def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

def save(self):
    sql = """
           INSERT INTO books (name, author, page_count, user_id, genre_id)
           VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name,self.author,self.page_count,self.user_id, self.genre_id,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

@classmethod
def create(cls, name, author, page_count, user_id, genre_id):
    user = cls(name,author, page_count, user_id, genre_id )
    user.save()
    return user

def update(self):
        sql = """
            UPDATE books
            SET name = ?, author = ?, page_count = ?,
            user_id = ?, genre_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.author,self.page_count,self.user_id, self.genre_id, self.id))
        CONN.commit()

def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

@classmethod
    def instance_by_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.name = row[1]
            book.author = row[2]
            book.author = row[3]
            book.page_count = row{4}
            book.user_id = row[5]
            book.genre_id = row[6]
        else:
            book = cls(row[1],row[2], row[3], row[4], row[5], row[6])
            book.id = row[0]
            cls.all[book.id] = book
        return book

@classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM boo
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_by_db(row) for row in rows]

@classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_by_db(row) if row else None

@classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT *
            FROM books
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_by_db(row) if row else None

@classmethod
def find_by_author(cls, author):
    sql= """
        SELECT *
        FROM books
        WHERE author = ?
    """
    row = CURSOR.execute(sql, (author,)).fetchone()
    return cls.instance_by_db(row) if row else None
    
