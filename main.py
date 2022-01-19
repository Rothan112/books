from books.BooksList import BooksList
from books.Book import Book
from books.Storage import Storage

# Press the green button in the gutter to run the script.
def add_book(my_books):
    title = input("title: ")
    author = input("author: ")
    genre = input("genre: ")
    status = input("status: ")
    newBook = Book(title, author, genre, status)
    my_books.add(newBook)
    my_books.print()


def search_title(my_books):
    title_to_search = input("title: ")
    given_title = my_books.searchTitle(title_to_search)
    print(given_title[0].title)


def search_author(my_books):
    author_to_search = input("author: ")
    given_author = my_books.searchAuthor(author_to_search)
    print(given_author[0].author)


def add_favorite(my_books):
    title = input("title: ")
    found_book = my_books.searchTitle(title)
    my_books.addFavorite(found_book[0])


def next_up(my_books):
    title = input("title: ")
    chosen_book = my_books.searchTitle(title)
    my_books.setNextUp(chosen_book[0])


if __name__ == '__main__':
    storage = Storage()
    myBooks = storage.readBookFile("./resources/books.csv")

    bookFunctions = True
    while bookFunctions:
        stuff = input("0- add book  1- search title  2- search author  3- add favorite  4- set Next Up  5- exit:  ")
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
            pass
        else:
            pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
