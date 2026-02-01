class person:
    name = "anuj"
    age = "19"
    occupation = "Soc analyst"

    def info(self): # self parameter is a reference to the current instance of the class
        print(f"{self.name} is a {self.occupation}")

a = person() # a is the object of class person
# a.name = "krishna"
# a.occupation = "student"     --> by this you can change 
# print(a.name,a.age)
# print(a.name)
a.info() 


"""
Constructoors :- 
default and parameterized constructors 
"""

print("\n\t constructor ! \t\n ")

class newperson :
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a1 = newperson("anuj", "footballer")
a1.info()



"""
Decorators :- allow you to modify the behaviour of functions and tools
Decorator is a function that takes another function as input and extends its behavior without modifying its source code.
made with @ --> for example @demo_decorator
"""

"""
Inheritance :- 
"""

class Employee :
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee {self.id} is {self.name}")

class Programmer(Employee):
    def showLangguage(self):
        print("the default language is python ")

e1 = Employee("anuj",1)
e1.showDetails()
e2 = Programmer("Anil",2)  # beta baap aur khud ki bhi dono quality dikhaega
e2.showDetails()
e2.showLangguage()

# e2.employee  it will be wrong 
e2.showLangguage  

print("\n\t Access Modifiers \t\n")

"""
Access Modifiers/specifiers
1> public access modifiers   -> by default
2> private access modifiers   -> to protect from being overwritten
3> protected access modifiers  -> intented to be used by thhe class itself and its subclasses 

Name mangling is a technique to protect the class-private / superclass-private variables that should not be overwritten by subclasses
"""

class e :
    def __init__(self):   # by default you make anything in python that will be public 
        self.name = "Anuj"

a1 = e()
print(a1.name)

class f :
    def __init__(self):   # __ before the variable make it private {__} -> it is known as weak internal indicator
        self.__name = "Anuj"

a2 = f()
# print(a2.__name)  -> it will throw error 

print(a2._f__name)  # method to acces the private variable 



# print("\n\t Library Management system (demo) \t\n")
"""
Library Management System :- 
Write a program to create a library from this library class and show you can print all books ,
 add a book and get the number of books using differnet methods , show that your progran doesnt persist the books after the program is stopped

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

print ("\n\t  Static Method  \n\t")
"""
static methods :- function under the class which does not uses self 
"""

class Mathtool:

    @staticmethod  # telling the compiler this function does not require object 
    def add(a,b):  # without this {@staticmethod} line python will think a = self, b = 2  --> mismatch 
        return a + b
    
print(Mathtool.add(1,2))


"""
OBJECT == INSTANCE 

When we talk about objects in a class, we mean the instance of that class.
class in the blueprint and object will be the part of that blueprint 

Agar data har object ka alag ho
→ instance variable

Agar data sabka same ho
→ class variable
"""


class Grocery:

    shop_name = "My Grocery"   # ← class variable

    def __init__(self, items):
        self.items = items     # ← instance variable , gets differed with objects/instances 

g1 = Grocery()
g1.items