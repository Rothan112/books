import operator
class NextUp:
    nextUp = []
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
        
    def searchTitle(self, title):
        return [x for x in self.list if x.title == title]
        
    def searchAuthor(self, author):
        return [x for x in self.list if x.author == author]

    # def nextUp(self):
    #     self.myList = nextUp(self.myList, key=operator.attrgetter(NextUp))
