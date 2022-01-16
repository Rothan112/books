from books.Book import Book
from books.BooksList import BooksList
import csv
class Storage:
    def __init__(self):
        pass

    def readBookFile(self, book_file):
        books = BooksList()
        with open(book_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                newBook = Book(row['title'], row['author'], row['genre'], row['status'])
                books.list.append(newBook)
        return books