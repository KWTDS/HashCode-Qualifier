from lib.library import Library
from lib.book import Book

files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

# user = int(input("input 1-5 (in order of smallest file to biggest): "))
file = [i.split(" ") for i in (open(files[0] + ".txt", "r").read().strip().split("\n"))]
numOfBooks, numOfLibs, days = [int(i) for i in file.pop(0)]
scores = [int(i) for i in file.pop(0)]



libs = list()
books = dict()

for i in range(numOfLibs):
	libBooks = list()
	library = file.pop(0)
	currBook = file.pop(0)
	for n in currBook:
		if int(n) in books:
			books[int(n)] = books[int(n)] + 1
		else:
			books[int(n)] = 1

	for n in books:
		libBooks.append(Book(n, scores[n], books[n]))

	libs.append(Library(i, int(library[1]), int(library[2]), libBooks))

# for day in range(days):
