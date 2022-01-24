import operator
class NextUp:
    nextUp = []
class BooksList:
    list = []

    def __init__(self):
        self.nextBook = None
        self.favorites = []

    def add(self, book):
        self.list.append(book)

    def print(self):
        for book in self.list:
            print(book.title + "\t\t\t\t\t\t\t\t\t\t\t" + book.author + "\t\t\t\t" + book.genre + "\t\t\t" + book.status)

    def sort(self):
        self.list = sorted(self.list, key=operator.attrgetter('title'))

    def addFavorite(self, favoriteBook):
        self.favorites.append(favoriteBook)
        
    def searchTitle(self, title):
        return [x for x in self.list if x.title == title]
        
    def searchAuthor(self, author):
        return [x for x in self.list if x.author == author]

    def searchFavorites(self, title):
        favorites = [x for x in self.favorites if x.title == title]
        if len(favorites) == 0:
            return True
        else:
            return False

    def setNextUp(self, myNextBookToRead):
        self.nextBook = myNextBookToRead
