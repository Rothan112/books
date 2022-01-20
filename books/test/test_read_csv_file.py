import unittest
import os
from books.Storage import Storage
from books.BooksList import BooksList
from books.Book import Book
from pathlib import Path


class CsvReaderTest(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()

    def test_canary(self):
        self.assertEqual(True, True)

    def test_can_read_csv_file(self):
        response = self.storage.readBookFile("../../resources/test/Sample_Books.csv")
        self.assertEqual(len(response.list), 1)
        self.assertTrue(isinstance(response, BooksList))

    def test_file_contains_NoLongerHuman_title(self):
        response = self.storage.readBookFile("../../resources/test/Sample_Books.csv")
        self.assertEqual(response.list[0].title, "No Longer Human")

    def test_can_write_csv_file(self):
        # arrange
        path = "../../resources/test/Sample_Books_SavedFile.csv"
        test_list = BooksList()
        test_book = Book("testtitle", "testauthor", "foogenre", "barstatus")
        test_list.add(test_book)
        # act
        self.storage.writeBookFile(test_list, "../../resources/test/Sample_Books_SavedFile.csv")
        actual = Path(path)
        # assert
        self.assertTrue(actual.is_file())
        os.remove(path)
