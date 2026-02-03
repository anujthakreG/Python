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
print(Emp.company)
# co.namee = "hehe"
print(co.company)   # this both will show the "Apple" in the output !

print("\n\t Next subtopic \n\t ")

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
A.sound()

"""
dunder method start with __ 
Operator overloading --> to change the behaviour of the operators 
"""