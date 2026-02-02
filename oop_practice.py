"""
Library Management System :- 
Write a program to create a library from this library class and show you can print all books ,
 add a book and get the number of books using differnet methods , show that your progran doesnt persist the books after the program is stopped
"""
class Library :
    
    book = []

    def __init(self):
        self.book = [] # empty list 

    
    def add_book(self,book_name):
        self.book.append(book_name)
        print(f"book {book_name} added in the list !")

    def show_book(self) :
        print("Books in library : ")
        for b in self.book:
            print(" - ",b)
    

    def get_total_books(self):
        print("total number of books in library : ")
        print(len(self.book))

lib = Library() # lib object creation 

lib.add_book("chris hamsworth")
lib.add_book("harry potter")

a = input("Enter the book to be added in library: ")
lib.add_book(a)


lib.show_book()

lib.get_total_books()

"""
Grocery Store :- 
"""

class Grocery :
    # count = 0  if you will declare the variable here then used this by self.var in every method for individually or it will not work

    item = []

    def __init__(self):
        self.item = []

    def add_item(self,item_name):
        self.item.append(item_name)
        print(f"{item_name} added in the list ")

    def show_items(self):
        print("gricery items !")
        for b in self.item:
            print(" - ", b)

    def total_item(self):  # total printing 1st method
        print("total items by 1st method :- ",len(self.item))


    def total_item2(self):
        count = 0
        for b in self.item:
            count = count + 1
        print("total items by 2nd method :- ",count)
            
i = Grocery()
i.add_item("Biscuits")
i.add_item("Krakjack")
i.add_item("dary milk")

i.show_items()
i.total_item()
i.total_item2()

print("\n\t  Playlist Manager \n\t")

"""
Create a class Playlist
It should:
store song names
add song
show all songs
count songs using two methods
"""

class Playist :

    song = []

    def __init__(self):
        self.song = []

    def add_song(self,song_name):
        self.song.append(song_name)
        print(f" {song_name} added ")

# it is similar to above question
    def show_song(self):
        print("songs present in the ")
        for b in self.song:
            print(" - ",b)

    def tot1(self):
        count = 0
        for b in self.song:
            count = count + 1
        print("total songs :- ",count)

s1 = Playist()

s1.add_song(" Channa vey !")
s1.add_song(" oh mahi !")
s1.add_song(" shararat ")

s1.show_song()
s1.tot1()

# ------------------------------------------------------------------------------------

