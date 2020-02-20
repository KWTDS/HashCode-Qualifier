from lib.library import Library
from lib.book import Book

files = ["a_example"]

# user = int(input("input 1-5 (in order of smallest file to biggest): "))
file = [i.split(" ") for i in (open(files[0] + ".txt", "r").read().strip().split("\n"))]
numOfBooks, numOfLibs, days = [int(i) for i in file.pop(0)]
scores = [int(i) for i in file.pop(0)]

libs = list()
books = dict()

signing = False

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
        print(n)
        libBooks.append(Book(n, scores[n], books[n]))

    libs.append(Library(i, int(library[1]), int(library[2]), libBooks))

libs.sort(key=Library.hscore, reverse=True)

signedLibs = list()

signedBooks = dict()

for day in range(days):
    if len(libs) > 0:
        library = libs[0]
        if not library.signup(day):
            signedLibs.append(libs.pop(0))

    if (len(signedLibs) > 0):
        for l in signedLibs:
            l.scanBooks()



# output = open("answers/" + files[0] + "_answer.txt", "w")
string = f'{len(signedLibs)}\n'
for i in signedLibs:
    string += f'{i.id} {len(i.scannedBooks)}\n'
    for n in i.scannedBooks:
        print(i.scannedBooks)
        string += f'{n.id} '
    string += "\n"
print(string)
# output.write(string)
