from books.Book import Book
import csv
class Storage:
    def __init__(self):
        pass

    def readCvs(self, file):
        return open(file)

    def readBookFile(self, book_file):
        books = []
        with open(book_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                newBook = Book(row['title'], row['author'], row['genre'], row['status'])
                books.append(newBook)
        return books