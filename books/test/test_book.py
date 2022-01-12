import unittest
from books.Book import Book

class BookTest(unittest.TestCase):
    def setUp(self):
        bookList = []

    def test_canary(self):
        self.assertEqual(True, True)

    def test_create_book(self):
        book = Book("title", "author", "genre", "status")
        self.assertIsInstance(book, Book)

    def test_add_book(self):
        book = Book("dummytitle", "stupidauthor", "badgenre", "yomom")
        bookList.add(book)