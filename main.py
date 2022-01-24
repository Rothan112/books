from books.BooksList import BooksList
from books.Book import Book
from books.Storage import Storage

# Press the green button in the gutter to run the script.
def add_book(my_books):
    title = input("title: ").strip()
    author = input("author: ").strip()
    genre = input("genre: ").strip()
    status = input("status: ").strip()
    newBook = Book(title, author, genre, status)
    my_books.add(newBook)


def search_title(my_books):
    title_to_search = input("title: ")
    given_title = my_books.searchTitle(title_to_search)
    print(given_title[0].title)


def search_author(my_books):
    author_to_search = input("author: ")
    given_author = my_books.searchAuthor(author_to_search)
    print(given_author[0].author)



def add_favorite(my_books):
    title = input("title: ").strip()
    if my_books.searchFavorites(title):
        found_book = my_books.searchTitle(title)
        try:
            my_books.addFavorite(found_book[0])
        except:
            print("Add book to book list before adding to favorites")
    else:
        print("Already favorited...")


def next_up(my_books):
    title = input("title: ")
    chosen_book = my_books.searchTitle(title)
    my_books.setNextUp(chosen_book[0])

def goodbye(my_books):
    storage.writeBookFile(my_books, "./resources/books.csv")
    storage.writeFavoritesFile(my_books, "./resources/favorites.csv")
    print("Exiting program. Goodbye...")
    exit()

if __name__ == '__main__':
    storage = Storage()
    myBooks = storage.readBookFile("./resources/books.csv")
    myBooks.favorites = storage.readFavoriteFile("./resources/favorites.csv")

    bookFunctions = True
    while bookFunctions:
        stuff = input("0- add book  1- search title  2- search author  3- add favorite  4- set Next Up  5- Print book list  6- exit:  ")
        if (stuff == "0"):
            add_book(myBooks)
        elif (stuff == "1"):
            search_title(myBooks)
        elif (stuff == "2"):
            search_author(myBooks)
        elif (stuff == "3"):
            add_favorite(myBooks)
        elif (stuff == "4"):
            next_up(myBooks)
        elif (stuff == "5"):
            myBooks.print()
        elif (stuff == "6"):
            goodbye(myBooks)
        else:
            pass
