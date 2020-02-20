files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

# user = int(input("input 1-5 (in order of smallest file to biggest): "))
file = [i.split(" ") for i in (open(files[0] + ".txt", "r").read().strip().split("\n"))]
numOfBooks, numOfLibs, days = [int(i) for i in file.pop(0)]
scores = [int(i) for i in file.pop(0)]

dictionaryOfLibs = dict()
books = dict()
for i in range(numOfLibs):
	library = file.pop(0)
	currBook = file.pop(0)
	dictionaryOfLibs[i] = [[int(x) for x in library], [int(x) for x in currBook]]

	for n in currBook:
		if n in books:
			books[n] = books[n] + 1
		else:
			books[n] = 1

print(dictionaryOfLibs, "\n", books)