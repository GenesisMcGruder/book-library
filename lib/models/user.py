from models.__init__ import CURSOR, CONN

class User:
    all = {}

    def __init__(self, name,password, id=None):
        self.id = id
        self.name = name
        self.password = password

    def __repr__(self):
        return f"User: {self.name} Password: {self.password}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string and between 1 and 15 characters")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password, int) and  len(password) == 6:
            self._password = password
        else:
            raise ValueError("Password must be a 6 digit code")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                password INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO users (name, password)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name,self.password,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, password):
        user = cls(name, password)
        user.save()
        return user

    def update(self):
        sql = """
            UPDATE users
            SET name = ?, password = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.password, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM users
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_by_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            user.name = row[1]
            user.password = row[2]
        else:
            user = cls(row[1],row[2])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM users
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_by_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_by_db(row) if row else None

    @classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT *
            FROM users
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_by_db(row) if row else None

    def books(self):
        from book import Book
        sql = """
            SELECT * FROM books
            WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [
            Book.instance_by_db(row) for row in rows
        ]
    


