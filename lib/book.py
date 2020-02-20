
def __hscore_compute(score,count):

class Book:
    def __init__(self,id,score):
        self.__hscore = None
        self.id = id
        self.count = 1
        self.score = score
        self.__dirty = True

    def dup(self):
        self.count += 1
        self.__dirty = True

    def hscore(self):
        if self.__dirty:
            self.__hscore = (1.5/self.count)*self.score
            self.__dirty = False
        return self.__hscore

