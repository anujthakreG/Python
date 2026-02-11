# 1) Greatest of Three Numbers 
# Write a function greatest(a, b, c) that returns the largest of three numbers. 

# def greatest(a,b,c):
#     if a > b and a > c :
#         return print(a,"is the greatest number")
#     elif b > c :
#         return print(b,"is the greatest number ")
#     else :
#         return print(c,"is the greatest number ")

# a = int(input("enter the first number :- "))
# b = int(input("enter the second number :- "))
# c = int(input("enter the third number :- "))
# greatest(a,b,c)



#   2) Factorial Function 

# def factorial(n):
#     prod = 1
#     for i in range (1,n+1):
#         prod = prod * i
#     return prod

# n = int(input("Enter the number :- "))
# print("the factorial of the number is :- ", factorial(n))



#  3) Palindrome Checker 
# Write a function is_palindrome(word) that returns True if the given string is a 
# palindrome, else False. 


# def is_palindrome(word):
#     reversed_word = ""        
#     for ch in word:            
#         reversed_word = ch + reversed_word  
#     return word == reversed_word



# print(is_palindrome("madam"))   
# print(is_palindrome("hello"))   



#  4) Prime Number Checker 
# Write a function is_prime(n) that returns True if a number is prime, else False. 

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):   
#         if n % i == 0:
#             return False
#     return True


# print(is_prime(7))  
# print(is_prime(10))  

# 5) Fibonacci Series Generator 
# Write a function fibonacci(n) that returns the first n numbers of the Fibonacci series.


# def fibonacci(n):
#     a, b = 0, 1              
#     print("Fibonacci series:")
#     for i in range(n):      
#         print(a, end=" ")    
#         a, b = b, a + b      

# n = int(input("Enter how many terms you want: "))
# fibonacci(n)


#   6) Sum of Digits 
# Write a function sum_of_digits(n) that returns the sum of digits of a given integer.

# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit
#         n //= 10
#     return total


# print(sum_of_digits(1234))   
# print(sum_of_digits(9876))  

# 7) Count Vowels in a String 
# Write a function count_vowels(s) that counts how many vowels (a, e, i, o, u) are in the 
# string.


# def count_vowels(s):
#     vowels = "aeiouAEIOU"   
#     count = 0
#     for ch in s:
#         if ch in vowels:
#             count += 1
#     return count


# print(count_vowels("Hello World"))  
# print(count_vowels("Python"))        


# 8) Find Maximum in a List 
# Write a function find_max(lst) that returns the maximum element from a list without 
# using max().


# def find_max(lst):
#     if not lst:   # check if list is empty
#         return None
#     maximum = lst[0]          # assume first element is max
#     for num in lst:
#         if num > maximum:
#             maximum = num
#     return maximum

# # Example usage
# print(find_max([3, 7, 2, 9, 5]))   # 9
# print(find_max([-10, -3, -50]))    # -3


#  9) Reverse a String 
# Write a function reverse_string(s) that returns the reversed version of a string.


def reverse_string(s):
    reversed_s = ""
    for ch in s:
        reversed_s = ch + reversed_s   # add each char in front
    return reversed_s

# Example usage
print(reverse_string("hello"))   # "olleh"
# print(reverse_string("python"))  # "nohtyp"






#  10) Check Armstrong Number 
# # Write a function is_armstrong(n) that checks whether a number is an Armstrong 
# # number.

# def is_armstrong(n):
#     digits = str(n)
#     power = len(digits)
#     total = 0
#     for d in digits:
#         total += int(d) ** power
#     return total == n

# # Example usage
# print(is_armstrong(153))   # True (Armstrong)
# print(is_armstrong(9474))  # True (Armstrong)
# print(is_armstrong(123))   # False

