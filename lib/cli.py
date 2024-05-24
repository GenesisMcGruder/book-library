from models.genre import Genre
from helpers import (
    quit,
    list_genres,
    list_books,
    add_book,
    add_genre,
    delete_book,
    delete_genre,
    selected_genre_books,
    selected_book_info
) 



def main_menu():
    print("**Welcome**")
    print("Genres")
    print("Choose from the following options then hit enter:")
    list_genres()
    print("G. Add a Genre")
    print("D. Delete a Genre")
    print("A. All Books")
    print("B. Add a Book")
    print("Q. Quit")


def main():
    menu_options = ['G', 'D','A', 'Q']
    genres = Genre.get_all()

    while True:
        main_menu()
        choice = input().upper()

        if choice == 'Q':
            quit()
        elif choice == 'G':
            add_genre()
        elif choice == 'D':
            delete_genre()
        elif choice == 'A':
            list_books()
        elif choice == 'B':
            add_book()
        elif choice.isdigit() and int(choice) <= len(genres):
            genre_index = int(choice) -1
            selected_genre = genres[genre_index]
            genre_book_menu(genres, genre_index, main) 
        else:
            print("Invalid choice. Please try again")   


def genre_book_menu(genres, genre_index, main):
    selected_genre = genres[genre_index]
    books = selected_genre.books()
    print(f'**{selected_genre.name}**')
    selected_genre_books(selected_genre)
    print("D. Delete a Book")
    print("B. Back")
    print("Q. Quit")

    menu_options = ['D','Q', 'B']

    while True:
        choice = input().upper()
        if choice == 'Q':
            quit()
        elif choice == 'D':
            delete_book()
        elif choice == "B":
            return main()
        elif choice.isdigit() and int(choice) <= len(books):
            book_index = int(choice) -1
            book_info_menu(books,book_index, genres, genre_index)
        else:   
            print("Invalid choice. Please try again.")

def book_info_menu(books, book_index, genres, genre_index):
    selected_book = books[book_index]
    print(f'**{selected_book.name}**')
    selected_book_info(selected_book)
    print("D. Delete Book")
    print("B. Back")

    menu_options = ['D','B']

    while True:
        choice = input().upper()
        if choice == 'D':
            delete_book()
            exit_menu = True
        elif choice == 'B':
            return genre_book_menu(genres, genre_index, main)
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()

