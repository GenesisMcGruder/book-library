from helpers import (
    quit,
    list_genres,
    list_books,
)
# this the genres loop
#welcome

def main():
    choice = 0
    while choice !=8:
         print("**Welcome**")
         print("Generes:")
         list_genres()
         print("5. Add a Genre")
         print("6. Delete a Genre")
         print("7. All Books")
         print("8. Quit")
         print("Please choose from the above options:")
         choice = int(input())

    if choice == 1:
        list_books()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        quit()


if __name__ == "__main__":
    main()


# def genres_loop():
#     #list the genres in DB , recieve back a list of all the genre
    
#     while True:
#         # call menu_1

#         choice = input(">")
#         if choice == "L":
#             logout()
#         else if  choice == "1":
#             menu_2()

#         elif #pick see details
#         #let user pick genre
#         #call genre_books_loop pass it the object they  pick



# # genre books loop

# def genre_books_loop():
#      while True:
#         # call menu_2

#         choice = input(">")
#         if choice == "L":
#             logout()
#         else if  choice == "1":
#             pass
#         #else if choice == go back:
#             # genres_loop()
        
# def logout():
#     exit()

# def menu_1():
#     # print("1. Users")
#     # print("2. Books")
#     # print("3. Genres")
#     print("list genres")
#     print("add genre")
#     print("delete genre") #delete genre books too
#     print("update genre")
#     print("pick to see details")

#     # print("4. Account")
#     print("L. Logout")

# def menu_2():
#     #list each genres book
#     #add
#     #delete
#     #back option
#     print("1. All Users")
#     print("2. Search Users")
#     print("L. Logout")


# def welcome():
#     print("Welcome!")

# def login():
#     print("Login:")

# def create_account():
#     print("Username not found, would you like to sign up? [y/n]")
    


