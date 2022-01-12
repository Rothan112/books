class BooksList:
    list = []

    def __init__(self):
        pass

    def add(self, book):
        self.list.append(book)

    def print(self):
        for book in self.list:
            print(book.title + "  " + book.author + "  " + book.genre + "  " + book.status)

    def sort(self):
        self.list.sort()
