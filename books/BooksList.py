import operator
class BooksList:
    list = []

    def __init__(self):
        self.favorites = []

    def add(self, book):
        self.list.append(book)

    def print(self):
        for book in self.list:
            print(book.title + "  " + book.author + "  " + book.genre + "  " + book.status)

    def sort(self):
        self.list = sorted(self.list, key=operator.attrgetter('title'))

    def addFavorite(self, favoriteBook):
        self.favorites.append(favoriteBook)
        
    def searchBook(self, BooksList):
        


