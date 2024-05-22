from models.book import Book
from models.genre import Genre

def quit():
    print("Goodbye!")
    exit()

def list_genres():
    genres = Genre.get_all()
    for index,genre in enumerate(genres, start=1):
        print(f'{index}. {genre.name}')

def list_books():
    books = Genre.books(1)
    print(f'{books}')