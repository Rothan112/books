import unittest
from books.BooksList import BooksList
from books.Book import Book

class BooksListTest(unittest.TestCase):
    def setUp(self):
        self.myBooks = BooksList()
        book1 = Book("badtitle", "smellyauthor", "dumbgenre", "GUH??")
        book2 = Book("fivetitle", "nightsauthor", "atgenre", "freddy'shouse")
        book3 = Book("goofytitle", "funnyauthor", "bubblygenre", "fun")
        book4 = Book("appletitle", "gamingauthor", "stupidgenre", "yAY")
        book5 = Book("zeustitle", "dadauthor", "urdumbgenre", "eatpoop")
        self.myBooks.add(book1)
        self.myBooks.add(book2)
        self.myBooks.add(book3)
        self.myBooks.add(book4)
        self.myBooks.add(book5)

    def test_canary(self):
        self.assertEqual(True, True)

    def test_add_book(self):
        book = Book("dummytitle", "stupidauthor", "badgenre", "yomom")
        self.myBooks.add(book)
        self.assertEqual(len(self.myBooks.list), 6)

    def test_sort_book(self):

        self.myBooks.sort()
        self.assertEqual("appletitle", self.myBooks.list[0].title)

    def test_add_book_to_favorite(self):
        favoriteBook = self.myBooks.list[0]
        self.myBooks.addFavorite(favoriteBook)
        self.assertTrue(favoriteBook in self.myBooks.favorites)
        
    def test_search_book(self):
        findBook = self.myBooks.BooksList[6]
        self.assertEqual(findBook, self.myBooks.searchBook(BooksList[6].title))
         
        
        

