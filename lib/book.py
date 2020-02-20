class Book:
    def __init__(self, id, score, count):
        self.__hscore = None
        self.id = id
        self.count = count
        self.score = score
        self.__dirty = True

    def hscore(self):
        if self.__dirty:
            self.__hscore = (1.5 / self.count) * self.score
            self.__dirty = False
        return self.__hscore
