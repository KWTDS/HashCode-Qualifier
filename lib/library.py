from lib.book import Book


class Library:
    def __init__(self, id, signt, booksperday, books):
        self.id = id
        self.signt = signt
        self.booksperday = booksperday
        self.books = books
        self.signing = False

    def timescore(self):
        self.signt + len(self.books) / self.booksperday

    def bscore(self):
        sum(map(lambda b: b.hscore(), self.books))

    def signup(self):
        self.signing = True
