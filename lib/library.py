from lib.book import Book


class Library:
    def __init__(self, id, signt, booksperday, books):
        self.id = id
        self.signt = signt - 1
        self.booksperday = booksperday
        # self.books = books.sort(key=Book.hscore, reverse=True)
        self.books = books
        self.scannedBooks = list()
        self.signing = False
        self.heuristic = None
        self.signDay = None

    def timescore(self):
        return self.signt + len(self.books) / self.booksperday

    def bscore(self):
        return sum(map(lambda b: b.hscore(), self.books))

    def hscore(self):
        return self.timescore() * 0.75 + self.bscore() * 0.25

    def scanBooks(self):
        # if (len(self.books) > 0):
        for i in range(min(self.booksperday, len(self.books))):
            self.scannedBooks.append(self.books.pop(0))

    def signup(self, day):
        if not self.signing:
            self.signing = True
            self.signDay = day
        elif day - self.signDay == self.signt and self.signing:
            self.signing = False
        return self.signing
