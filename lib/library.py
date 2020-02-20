from lib.book import Book


class Library:
    def __init__(self, id, signt, booksperday, books):
        self.id = id
        self.signt = signt - 1
        self.booksperday = booksperday
        self.books = books
        self.signing = False
        self.heuristic = None
        self.signDay = None

    def timescore(self):
        return self.signt + len(self.books) / self.booksperday

    def bscore(self):
        return sum(map(lambda b: b.hscore(), self.books))

    def hscore(self):
        self.heuristic = self.timescore() * 0.75 + self.bscore() * 0.25
        return self.heuristic

    def signup(self, day):
        if not self.signing:
            self.signing = True
            self.signDay = day
        elif day - self.signDay == self.signt and self.signing:
            self.signing = False
        # print(f'{day}, {self.signDay}, {day - self.signDay}')

        return self.signing
