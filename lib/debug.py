from models.__init__ import CONN, CURSOR
from models.user import User
import ipdb


def reset_database():
    Genre.drop_table()
    Book.drop_table()
    User.drop_table()
    User.create_table()
    Book.create_table()
    Genre.create_table()
    


    karen = User.create("Karen", 1234)
    leroy = User.create("Leroy", 5678)
    lucy = User.create("Lucy", 1616)
    herold = User.create("Herold", 1999)

    bible = Book.create("Bible AMP", "God", 1408, 3, 1)
    living_fearless = Book.create("Living Fearless", "Jamie Winship", 170, 1, 1)
    kingdom_culture = Book.create("Kingdom Culture", "Dan Farrelly", 365, 2, 1)
    the_way_of_life = Book.create("The Way of Life", "Bill Johnson", 224, 4, 1)


    religion = Genre.create("Religion")
    fiction= Genre.create("Fiction")
    memoir = Genre.create("Memoir")
    historical = Genre.create("Historical")

    


reset_database()
ipdb.set_trace()