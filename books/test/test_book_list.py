import unittest
from books.BooksList import BooksList
from books.Book import Book

class BooksListTest(unittest.TestCase):
    def setUp(self):
        self.myBooks = BooksList()

    def test_canary(self):
        self.assertEqual(True, True)

    def test_add_book(self):
        book = Book("dummytitle", "stupidauthor", "badgenre", "yomom")
        self.myBooks.add(book)
        self.assertGreater(len(self.myBooks.list), 0)

    def test_sort_book(self):
        book1 = Book("badtitle", "smellyauthor", "dumbgenre", "GUH??")
        book2 = Book("fivetitle", "nightsauthor", "atgenre", "freddy'shouse")
        book3 = Book("goofytitle", "funnyauthor", "bubblygenre", "fun")
        book4 = Book("appletitle", "gamingauthor", "stupidgenre", "yAY")
        book5 = Book("Zeustitle", "Dadauthor", "urdumbgenre", "eatpoop")
        self.myBooks.add(book1)
        self.myBooks.add(book2)
        self.myBooks.add(book3)
        self.myBooks.add(book4)
        self.myBooks.add(book5)
        self.myBooks.sort()
        self.assertEqual("appletitle", self.myBooks.list[0].title)
