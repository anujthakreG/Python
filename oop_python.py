class person:
    name = "anuj"
    age = "19"
    occupation = "Soc analyst"

    def info(self): # self parameter is a reference to the current instance of the class
        print(f"{self.name} is a {self.occupation}")

a = person() # a is the object of class person
# a.name = "krishna"
# a.occupation = "student"     #--> by this you can change 
# print(a.name,a.age)
# print(a.name)
# a.info() 
# print(person.occupation)
# print(a.occupation)

"""
Constructoors :- 
default and parameterized constructors 
whenerver you create a constructor wither you have to declare the variable or assume variable as no input  
so while creating object of that particular class you always have to pass the argument value  
Python does not support multiple contructors(__init__) -> so it is thereby replaced by @classmethod
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

class Employee :  # -> parent class 
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee {self.id} is {self.name}")

class Programmer(Employee):  # -> child class
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

print(a2._f__name)  # method to acces the private variable   {obj._classname.__varname}



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


# class Grocery:

#     shop_name = "My Grocery"   # ← class variable

#     def __init__(self, items):
#         self.items = items     # ← instance variable , gets differed with objects/instances 

# g1 = Grocery()
# g1.items

print("\n\t Next subtopic \n\t ")


"""
class method , deecorator name -> @classmethod -> works on the class variables not on the objects 
"""

# exmaple :
class Emp :
    
    company = "Apple"
    def show(self):
        print(f"{self.name} works in the company {self.company}")

    @classmethod
    def changecompany(cls, Newname):  # you can write anything in the place of cls 
        cls.company = Newname

co = Emp()
co.name = "Anuj"
co.show()
co.changecompany("tesla")
co.show()
print(Emp.company) # class Variable is called like this 
# co.namee = "hehe"
print(co.company)   # this both will show the "Apple" in the output !

print("\n\t Continuing Class-Method \n\t ")

"""
Class Methods as alternative contructors 
constructors are special type of method which automatically gets executed at the time of object creation 
there are times when you want to create object in a different manner so for that this method is usefull instead using the default contrucotr for it 
"""

# numbers = [int(x) for x in input("Enter numbers: ").split()]
# print(numbers)
 
class Employee2:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal


    @classmethod
    def fromstr(cls,String):
        return cls(String.split("-")[0] ,String.split("-")[1])
    
e22 = Employee2("john","120")
print(e22.name)
print(e22.sal)

String = "johra-1200"

# ee22.fromstr(String)  # it will throw error as the arguments are not passed while creating the object ee22
ee22 = Employee2.fromstr(String)

# string2 = input().split()   -> not working 
# ee3 = Employee2.fromstr(string2)


print("\n\t Next subtopic \n\t ")

"""
dir,__dict__,help methods in python 
"""

# x = [1,2,3]
# print(dir(x)) # -> "what things are available"
# # print(__dict__(e22))  # -> "what data is stored ?" 
# print(help(x))  # -> help you with the "how does it work"


print("\n\t Next subtopic \n\t ")

"""
super keyword -> used to refer the parent class 

"""

class Parentclass :
    def Parentmethod(self):
        print("this is Parent class method")

class Childclass(Parentclass):
    def Childmethod(self):
        print("this is child method ")

        super().Parentmethod()

c = Parentclass()
c.Parentmethod()
c1 = Childclass()
c1.Childmethod()

"""
Dunder Method :- 
| Dunder Method              | Triggered by                      | Purpose                                               |
| -------------------------- | --------------------------------- | ----------------------------------------------------- |
| `__init__(self, ...)`      | Object creation → `obj = Class()` | Initializes the object (constructor)                  |
| `__str__(self)`            | `print(obj)`                      | Returns user-friendly string representation of object |
| `__len__(self)`            | `len(obj)`                        | Returns length of the object                          |
| `__add__(self, other)`     | `obj1 + obj2`                     | Defines addition behaviour for objects                |
| `__eq__(self, other)`      | `obj1 == obj2`                    | Defines equality comparison                           |
| `__getitem__(self, index)` | `obj[index]`                      | Enables indexing access                               |

"""
"""
Method overridding -> method name , parameters must be same and it must be inherited 
"""

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

A = Dog()
B = Animal()
A.sound()
# B.sound()

"""
dunder method start with __ 
Operator overloading --> to change the behaviour of the operators 
"""

"""
Single Inheritance :- where a class inherits the property from a Single parent class ,default one
Multiple Inheritance :- child class made by more than 1 parent class 
Multilevel Inheritance :- Parentclass --> childclass1 --> childclass2(child of childclass1)
"""

# example for multiple inheritance ->

class Employee:
    def __init__(self,name):
        self.name = name

        print(f"the name is {self.name}")

    def show(self):
        print(f"the name is {self.name}")

class Dancer:

    def __init__(self,dance):
        self.dance = dance 

    def show(self):
        print(f"the dance is {self.dance}")
                                # -> method overriding is here 
class EmployeeDancer(Employee, Dancer) : # -> if you write Employee parentclass first then that class method will run first
# class EmployeeDancer(Dancer,Employee) :
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

o = EmployeeDancer("hariss-ALI-Khan","HipHop")
print(o.name)
print(o.dance)

o.show()




