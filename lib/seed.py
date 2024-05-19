from models.__init__ import CONN, CURSOR
from models.user import User
# from models.scripture import Scripture

def seed_database():
    User.drop_table()
    User.create_table()

    
    karen = User.create('Karen')
    leroy = User.create("Leroy")
    lucy = User.create("Lucy")
    herold = User.create("Herold")


seed_database()
print("Seeded Database")