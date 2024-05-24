from models.__init__ import CONN, CURSOR
from models.book import Book
from models.genre import Genre
from helpers import list_books
import ipdb


def reset_database():
    Genre.drop_table()
    Book.drop_table()
    Book.create_table()
    Genre.create_table()
    


    # karen = User.create("Karen", 1234)
    # leroy = User.create("Leroy", 5678)
    # lucy = User.create("Lucy", 1616)
    # herold = User.create("Herold", 1999)

    religion = Genre.create("Religion")
    fiction= Genre.create("Fiction")
    memoir = Genre.create("Memoir")
    historical = Genre.create("Historical")

  
    bible = Book.create("Bible AMP", "God", 1408, 1)
    living_fearless = Book.create("Living Fearless", "Jamie Winship", 170, 1)
    kingdom_culture = Book.create("Kingdom Culture", "Dan Farrelly", 365, 1)
    the_way_of_life = Book.create("The Way of Life", "Bill Johnson", 224, 1)
    lotr_pt1 = Book.create("Fellowship of the Ring", "J.R.R. Tolkien", 479, 2)
    johnny_tremain = Book.create("Johnny Tremain", "Esther Forbes", 212, 4)
    im_glad_my_mom_died = Book.create("Im Glad My Mom Died", "Jennette McCurdy", 320, 3)
    hunger_games = Book.create("Hunger Games", "Suzanne Collins", 384, 2)
    catching_fire = Book.create("Catching Fire", "Suzanne Collins", 391, 2)
    two_towers = Book.create("Two Towers", "J.R.R. Tolkien", 416, 2)
    you_can_be_free = Book.create("You can be Free", "Kirby Kelly", 240, 1)
    counting_the_Cost = Book.create("Counting the Cost", "Jill Duggar", 287, 3)
    the_woman_in_me = Book.create("The Woman in Me", "Britney Spears", 288, 3)
    red_notice = Book.create("Red Notice", "Bill Browder", 416, 3)
    carry_on_mr_bowditch = Book.create("Carry on MrBowditch", "Jean  Lee Latham", 251, 4)
    the_hiding_place = Book.create("The Hiding Place", "Corrie ten Boom, John and Elizabeth Sherrill", 272, 4)
    number_the_stars = Book.create("Number the stars", "Lois Lowry", 137, 4)



    
reset_database()
ipdb.set_trace()