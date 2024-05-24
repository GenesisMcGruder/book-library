from models.book import Book
from models.genre import Genre

def quit():
    print("Goodbye!")
    exit()


def list_genres():
    genres = Genre.get_all()
    for index,genre in enumerate(genres, start=0):
        print(f'{index +1}. {genre.name}')


def list_books():
    books = Book.get_all()
    for index,book in enumerate(books, start=1):
        print(f'{index}. {book.name}')

def selected_genre_books(selected_genre):
    books = selected_genre.books()
    for index,book in enumerate(books, start = 1):
        print(f'{index}. {book.name}')

def selected_book_info(selected_book):
    book = selected_book.find_by_id(selected_book.id)
    print(f'Author: {book.author}') 
    print(f'Page Count: {book.page_count}')
def add_genre():
    name = input("Enter new genre: ")
    try:
        genre = Genre.create(name)
        print(f'Genre: {name} is successfully created!')
    except Exception as exc:
        print("Error creating new genre: ", exc)

def add_book():
    name = input("Enter new book name: ")
    author = input("Enter author: ")
    page_count = int(input("Enter page count: "))
    genre_name = input("Enter genre: ")
    try:
        genre = Genre.find_by_name(genre_name)
        if genre is None:
            raise ValueError("Invalid genre id")
        genre_id = genre
        book = Book.create(name, author, page_count, genre_id)
        print(f'Book: {name} successfully added')
    except Exception as exc:
        print("Error creating adding a new book: ", exc)


def delete_genre():
    name = input("Enter genre name to be deleted: ")
    genre = Genre.find_by_name(name)
    if genre is not None:
        Genre.delete(genre)
        print(f'Genre {name} has been successfully deleted')
    else:
        print(f'Genre {name} not found')

def delete_book():
    name = input("Enter book name to be deleted: ")
    if book == Book.find_by_name(name):
        book.delete()
        print(f'Book {name} has been deleted successfully')
    else:
        print(f'Boof {name} has not been found')


