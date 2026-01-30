# [Output --> loop --> condition ]  --> this is the general condition for the comprehension 


list = ["suzuki", "Sedan" ,"Smc" ,"Mini"]
New_list = []
for x in list:
    if "S" in x:
        New_list.append(x)

print(list)
print(New_list)

# List compression

list1 = ["suzuki", "Sedan-Ev" ,"Smc-Ev" ,"Mini"]
New_list1 = [ x for x in list1 if "Ev" in x ]

print(list1)
print(New_list1)

#--------------------------------------

list2 = [1,2,3,4,5,6]
New_list2 = []

for x in range(1,5):
    x = x * x 
    New_list2.append(x)

print(list2)
print(New_list2)

#--------------------------------------

numbers = [1, 2, 3, 4, 5]    # this is how list is defined 
squares = [n * n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
# e = [n * n for n in numbers if n % 2 == 0]   
# print(squares , evens , e)
print(squares , evens )

#--------------------------------------


x = [x for x in range(1,10) if x % 2 == 0]
print(x)

#--------------------------------------

xx = [x for x in "python programming" if x in ['a','e','i','o','u']]
print(xx)

#--------------------------------------

mixed = [1,2,"a",3,4.2]
[x**2 for x in mixed if type(x) == int]
print(mixed)
print("yesss :- ",x)

#--------------------------------------

heh = [x + 3 for x in [1,2,3]]

print(heh)

#--------------------------------------
# create a generator eexpression to generate the squares fo numbers 0 to 9 
square_gen = (x * x for x in range(10))
print(square_gen)

# Sum of the squares of even numbers from 0 to 9 
# total_sum = [x for x * x in range(10)if x % 2 == 0]
# print(" the total sum is :- ", total_sum)
# print(f"the sum is : {total_sum}")
