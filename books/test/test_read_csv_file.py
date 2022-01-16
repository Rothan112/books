import unittest
from books.Storage import Storage
from books.BooksList import BooksList

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
        self.assertEqual(response[0].title, "No Longer Human")
