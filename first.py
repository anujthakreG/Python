"""
IMP -> for full detail visit the downloaded pdf

pip -> it is used to install modules(codes written by other ) on your own system for ex :- pip install pyjokes
import module_name 

"""

# import pyjokes
# jokes = pyjokes.get_joke()
# print(jokes)

# how to print multi-lines ?
"""
print('''
tu agar meri ye duao mai hai 
ehera hua 
''')
"""

"""
Python is a fantastic language that automatically identifies the type of data for us
"""

# Type Function and type casting :- 
# a = 2
# print(type(a))

# b = "3"
# type(b)

# for conversion ,str(3){integer to string } , int("3"){string to integer}

"""
-----------------------------------------------------------------------------------------------------------
Practice set :- 
1. Write a python program to add two numbers.
2. Write a python program to find remainder when a number is divided by z.
3. Check the type of variable assigned using input () function.
4. Use comparison operator to find out whether ‘a’ given variable a is greater than
‘b’ or not. Take a = 34 and b = 80
5. Write a python program to find an average of two numbers entered by the user.
6. Write a python program to calculate the square of a number entered by the user.
"""

# a = 2
# b = 1
# print(a + b )

# z = int(input("enter the number z :- "))
# n = int(input("eter the number n :- "))
# print(n % z)

# a = 2
# print(type(a))

# a = 34
# b = 80 
# if a > b :
#     print("a greater ")
# else :
#     print("b greater")

"""
-----------------------------------------------------------------------------------------------------------
Strings :- 
"""
"""
name = "jitendra"

nameshort = name[0:3] # start from the begining till the the third one ( excluidng the third )
print(nameshort)

# from startung the count if form 0 and from the last the counting is fro (-1)

nameshort1 = name[-4:-1]
print(nameshort1)



-----------------------------------------------------------------------------------------------------------
Strings practice set :- 
"""

# a = input("enter the word you want :- ")
# print(a,"Good afternoon")
"""
# hwo to take multiple user input in various ways :- 
# 1st :- Using split()
# Example: Taking multiple integers in one line
"""

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))  # the common way , (map) coverts each piece into int , split() seperate from the place where spcae is pressed  
# print("You entered:", numbers)

# numbersf = list(map(float, input("Enter numbers separated by space: ").split()))
# print("You entered for decimal numbers :- ", numbersf)

# okay = input().split()   # for entering the strings 
# print(okay)

# """
# 2nd way :- using fixed number of input
# """

# a, b, c = map(int, input(("enter three numbers :- ")).split())
# print("three numbers are :- ",a,b,c ,"respectively !")


# """
# 3rd way :- List comprehension
# """

# numbers = [int(x) for x in input("Enter numbers: ").split()]
# print(numbers)


"""
-----------------------------------------------------------------------------------------------------------
"""

# # Dictionaries and lists !
# marks = {
#     # "key" : "value"
#     "harry":20,
#     "wow":30,
#     0 : "hehe"
# }

# dictionary[key] = value


# print(marks.items())

# dict = {} # for making empty dictionary
# # Sets :- 
# set = {1,5,32}
# e = set() # for making empty set 

"""
-----------------------------------------------------------------------------------------------------------
dict and sets practice set :-
"""

# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
ps = {
    "key" : "value",
    "food" : "bhojan",
    "dance" : "nachna"
}
print("enter number for following activities :- ")
print("1 for full / 2 for english word /3 for hindi word")
no = input("enter the number :- ")
if no == 1:
    print(ps.items())
elif no == 2:
    print(ps.keys())
else :
    print(ps.values())

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
numbers = list(map(int, input("Enter numbers separated by space: ").split())) 
s = set()
for x in numbers :
    s.add(x)   # write all the methods for both dict and sets 

print(s)


# 3 .Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique

# Create an empty dictionary
fav_lang = {}

# Taking input from 4 friends
for i in range(4):
    name = input("Enter friend's name: ")
    language = input("Enter favorite language: ")
    fav_lang[name] = language

# Printing the dictionary
print("Favorite languages of friends:")
print(fav_lang)


"""
Practice Set :- 
"""

#   1) Greatest of Three Numbers 
# Write a function greatest(a, b, c) that returns the largest of three numbers. 
"""
def greatest(a,b,c):
    if a > b and a > c :
        print("greatest number is :- ",a)
    elif b > c :
        print("greates number  is :- ",b)
    else :
        print("greatest number is :- ",c)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
greatest(a,b,c)
"""

# 2) Factorial Function 
# Write a function factorial(n) that returns the factorial of a number n. Implement both 
# iteration and recursion. 
"""
def factorial(n):
    prod = 1
    while(n != 0):
        prod = prod * n
        n = n - 1
    print(prod)

a = int(input("enter the number :- "))
factorial(a)
"""


#3) Palindrome Checker 
# Write a function is_palindrome(word) that returns True if the given string is a 
# palindrome, else False. 
"""
palindrome :- naman

def is_palindrome(word):
    new_word = word
    sliced = word[::-1]
    if sliced == new_word:
        print("entered word is a pallindrone !")

word = input("enter the word :- ")
is_palindrome(word)
"""

# 4) Prime Number Checker 
# Write a function is_prime(n) that returns True if a number is prime, else False. 
"""
prime number? -> that is divisible bt itself and 1 


def is_prime(n):
    if n%1 == 0 and n % n == 0 :
        print("number is prime !")

n = int(input("enter the number :- "))
is_prime(n)
"""


# 5) Fibonacci Series Generator 
# Write a function fibonacci(n) that returns the first n numbers of the Fibonacci series.

# 6) Sum of Digits 
# Write a function sum_of_digits(n) that returns the sum of digits of a given integer. 
"""


def sum_of_digits(n):
    total = 0
    while n != 0:
        digit = n % 10 
        total = total + digit
        n = n // 10 
    print(total)

n = int(input("enter the number :- "))
sum_of_digits(n)
"""



# 10.   10) Check Armstrong Number 
# Write a function is_armstrong(n) that checks whether a number is an Armstrong 
# number.
"""
def is_armstrong(n):
    whole_no = n
    total = 0
    while n != 0:
        digit = n % 10 
        total = total + (digit* digit * digit)
        n = n // 10 
    if whole_no == total:
        print("yes it is ! ")     #it is unreachable coz return statment ends the function clearly
    else :
        print("no it is not !")
    

n = int(input("enter the number :- "))
is_armstrong(n)

"""
"""
---------------------------------------------------------------------------------------------------------------------------
"""
"""
# Wateer jug problem 
def water_no_bfs():
    # initial status 
    jug5 = 0
    jug3 = 0
    print("value :- ",jug5,jug3)

    # Step 1 :- initialization
    jug5 = 5 # <5,0>
    transfer = min(jug5, 3 - jug3)
    jug5 = jug5 - transfer
    jug3 = jug3 + transfer 
    print("jug5 :- ",jug5,"jug3 :- ",jug3)   #<2,3>

    #
    jug3 = 0
    print("jug5 :- ",jug5,"jug3 :- ",jug3)  #<2,0>

    #
    transfer = min(jug5, 3 - jug3)   #min(2,3) -> 2
    jug5 = jug5 - transfer
    jug3 = jug3 + transfer
    print("jug5 :- ",jug5,"jug3 :- ",jug3)  #<0,2>

    #
    jug5 = 5 #<5,2>
    transfer = min(jug5, 3 - jug3)  #min(5,1) -> 1 
    jug5 = jug5 - transfer
    jug3 = jug3 + transfer
    print("jug5 :- ",jug5,"jug3 :- ",jug3)  #<4,3>

water_no_bfs()


# Jug A capacity = 3 litres
# • Jug B capacity = 4 litres
# • Goal = 1 litre

def water_jug2_nobfs():
    jug3 = 0
    jug4 = 0
    print("value :- ",jug4,jug3)

    jug4 = 4 #<4,0>
    print("jug4 :- ", jug4, "jug3 :- ",jug3)

    t = min(jug4,1 - jug3) #min(4,1) -> 1
    jug4 = jug4 - t
    jug3 = jug3 + t
    print("jug4 :- ", jug4, "jug3 :- ",jug3)
    
    print("GOAL ACHIEVED")


water_jug2_nobfs()


"""
"""
---------------------------------------------------------------------------------------------------------------------------
Dfs :- depth first search -> water jug prroblem 
"""