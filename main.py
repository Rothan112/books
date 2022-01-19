from books.BooksList import BooksList
from books.Book import Book
from books.Storage import Storage

# Press the green button in the gutter to run the script.
def add_book(myBooks):
    title = input("title: ")
    author = input("author: ")
    genre = input("genre: ")
    status = input("status: ")
    newBook = Book(title, author, genre, status)
    myBooks.add(newBook)
    myBooks.print()

if __name__ == '__main__':
    storage = Storage()
    myBooks = storage.readBookFile("./resources/books.csv")

    bookFunctions = True
    while(bookFunctions):
        stuff = input("0- add book  1- search title  2- search author  3- add favorite  4- set Next Up  5- exit:  ")
        if (stuff == "0"):
            add_book(myBooks)
        elif (stuff == "1"):
            pass
        elif (stuff == "2"):
            pass
        elif (stuff == "3"):
            pass
        elif (stuff == "4"):
            pass
        elif (stuff == "5"):
            pass
        else:
            pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
