# [Output --> loop --> condition ]  --> this is the general condition for the comprehension 

""" 
About list comprehension and generator function 
Question 1 :- 
 Given a large range of numbers (eg. 1 to 100), create a generator expression to produce only the even numbers squares, 
filtering out odds, and iterate over it to sum the first 10 results. This simulates processing big data lazily: 
compute squares of evens like 74, 416, without storing the entire sequence upfront.
"""
""" Question number 2 :- 
 Given a list of numbers from 1 to 10, use a list comprehension to create a new list containing only the even numbers multiplied by 3. 
 Print the result to verify. Input: numbers l(range(1.11)) # (1,2,3, 10]Expected Output: [6, 12, 18, 24,30] 
   """

# Question 2 :- 
# solved by the general method 

list = [1,2,3,4,5,6,7,8,9,10]
new_list = []

for x in list :
    if x % 2 == 0:
        new_list.append(x * 3)

print(new_list)

# ques 2 lets solve by the list comprehension method 

# [Output --> loop --> condition ]  --> this is the general condition for the comprehension 

list1 = [1,2,3,4,5,6,7,8,9,10]
new_list1 = [x * 3 for x in list1 if x % 2 == 0]

print(new_list1)

#-----------------------------------------------------------------------------------------------------------------

# Question 1 :- 
gen = (x**2 for x in range(1,101) if x % 2 == 0)
print(gen)


# other way for executing this 
list3 = []
for i in range(100):      # starting no -> 0 , end no -> 99 
# for i in range(101)    -> end no -> 100 
    if i % 2 == 0:
        i = i * 2
        list3.append(i)

print(list3)



"""
Docstring for adv_practice
"""

transactions= [
    #(tid,item,amnt,status)
    
   (101,"pen",10,"paid"),
   (102,"book",120,"pending"),
   (103,"bag",850,"paid"),
   (104,"pen",10,"paid"),
   (105,"laptop",4500,"paid"),
   (106,"mouse",500,"pending")
]

# 1. Unique items from transactions
# usimg sets to get uniquue value basically -> result = [WHAT_YOU_WANT for ... in data]

unique_items = {item for _,item,_,_ in transactions}  
print("Unique items :- ",unique_items)

# 2. Dictionary mapping transaction id to amount
id_to_amount = {tid:amount for tid,_,amount ,_ in transactions}
print("ID to amount :- ", id_to_amount)

# 3. All transactions where status is "paid"
paid_transactions = [t for t in transactions if t[3] == "paid"]
print("paid transactions :- ", paid_transactions)

# 4. Amounts of transactions where status is "paid"
paid_amounts = [amount for _, _, amount, status in transactions if status == "paid"]

# 5. GST amounts (18% added) for paid amounts


# 6. (item, amount) pairs for paid transactions

"""
-----------------------------------------------------------------------------------------------------------------------
Question 2 :- student transaction practice 
"""
print("\n\t Second Question ! \t")
students = [
    (1, "Rahul", 85, "pass"),
    (2, "Anita", 72, "pass"),
    (3, "Rohit", 40, "fail"),
    (4, "Neha", 90, "pass"),
    (5, "Aman", 35, "fail")
]

# Q1️⃣ Create a set of unique names.
unique_names = {name for _,name,_,_ in students }
print("Unique names are :- ", unique_names)

# Q2️⃣Create a list of marks of only passed students.
passed_students = [marks for _, _, marks, status in students if status == "pass"]
print("list of marks :- ",passed_students)

# Q3️⃣Create a dictionary mapping roll_no → name.
roll_to_name = {uid:name for uid,name,_,_ in students}
print("roll no : name ",roll_to_name)

# Q4️⃣ Create a list of (name, marks) for students who failed.
failed_students = [(name, marks) for _, name, marks, status in students if status == "fail"]
print("failed students detail :- ",failed_students)

# Q5️⃣ Create a set of roll numbers where marks ≥ 80.
set_roll = {roll for  roll,_,marks,_, in students if marks >= 80}
print("set of roll numbers :- ",set_roll)

# Q6️⃣ Create a dictionary mapping name → marks only for passed students.
name_to_marks = {name:marks for _,name,marks,_ in students}
print("Name : marks ",name_to_marks)

name_to_status = {name:status for _,name,_,status in students}
print("name : status",name_to_status)

# 7️⃣ Create a list of marks increased by 5 for passed students only.
print("before incremention of pass students :- ")
normal_marks = [marks for _,_,marks,status in students if status == "pass"]
print(normal_marks)
marks_increased = [(marks + 5) for _,_,marks,status in students if status == "pass" ]
print("list of marks increased by 5 for passed students only",marks_increased)

# Q8️⃣ Create a list of names of students who scored less than 50.
stu_50 = [names for _,names,marks,_ in students if marks <= 50]
print("names of students who scored less than 50", stu_50 )

# Q9️⃣ Create a list of tuples (roll_no, result) for all students.
list_of_tuple = [(roll_no, result) for roll_no,_,_,result in students]
print("list of tuple :- ",list_of_tuple)



"""
---------------------------------------------------------------------------------------------------------
"""

"""
Docstring for ass1
6. Smart City Utility Consumption Monitoring:
A smart city system logs household utility usage data as tuples (house_id, utility_type,
consumption_units, payment_status). Using Python comprehensions, extract unique utility
types, filter completed payments, compute billing amounts based on unit cost, and calculate
total consumption per utility type.

"""

smart_city = [
    [1,"sewage",123,"paid"],
    [2,"water",123,"paid"],
    [3,"electricty",123,"paid"],
    [4,"sewage",123,"paid"],
    [1,"water",123,"paid"],
    [5,"transport",123,"paid"]
]

unit_costs = {
    "sewage": 2,
    "water": 3,
    "electricty": 5,
    "transport": 10
}

# using sets
unique_utility = {utility for _,utility,_,_ in smart_city}
print("unique utility types :- ",unique_utility)

complete_payment = [(id,type,payment,status )for id,type,payment,status in smart_city if status == "paid" ]
print("paid filtered list :- ",complete_payment)

biling_amount = [(id,utility , units *unit_costs[utility] , status ) for id,utility,units ,status in smart_city
                 if status == "paid" ]
print("biling amount based on unit cost :- ",biling_amount)

# new qyestion type
utilities = {utility : sum(unit for _,u,unit,_ in smart_city if u == utility ) for _,utility,_,_ in smart_city }
print("total consumption per utility type :- ",utilities)


print("\n\t  hospital  \n\t")

"""
4. Hospital Patient Billing and Treatment Summary:
A hospital maintains patient billing records as tuples (patient_id, treatment_type,
bill_amount, payment_status). Using Python comprehensions, extract unique treatment
types, map patient IDs to bill amounts, filter patients who have completed payment,
compute bills including service charges, and calculate the total revenue per treatment type.
"""

hospital = [
    [1,"leg",200,"paid"],
    [2,"hand",100,"paid"],
    [3,"heart",20000,"paid"],
    [4,"head",500,"paid"],
    [5,"stomach",250,"paid"],
    [6,"hand",100,"paid"],
    [7,"leg",200,"paid"]
]

service_charges = {
    "leg" : 50,
    "hand" : 60,
    "heart" : 80,
    "head" : 100,
    "stomach" : 20
}

unique_treatment = {type for _,type,_,_ in hospital}

id_to_bil = {id : amnt for id,_,amnt,_ in hospital}

filter_patient = [(id,type,amnt,status ) for id,type,amnt,status in hospital if status == "paid"]

bills_service_charge = [
    (id, type, amnt + service_charges[type], status)
    for id, type, amnt, status in hospital
    if status == "paid"
]

print("bills_service",bills_service_charge)

total_revenue = {type : sum(amnt for _,t,amnt ,_ in hospital if t == type) for _,type,_,_ in hospital}
print("total revenue generated by the hospital per type :- ", total_revenue)


print("\n\t Employee System \n\t")

"""
3. Employee Payroll and Department Analysis:
A company stores employee payroll data as a list of tuples (employee_id, department,
salary, employment_status). Write a Python program using comprehensions to identify all
unique departments, map employee IDs to their salaries, filter employees who are currently
active, compute revised salaries after applying a percentage increment, and calculate the
total salary expenditure per department.
"""

Employee = [
    [1,"robo",1000,"permanent"],
    [2,"aiml",10000,"permanent"],
    [3,"robo",1000,"temporary"],
    [4,"cse",21000,"permanent"],
    [5,"HR",100000,"temporary"],
    [6,"hod",1000,"permanent"],
    [7,"HR",100000,"temporary"]
]

unique_dep = {dep for _,dep,_,_ in Employee}
print("",unique_dep)

id_to_sal = {id : salary for id,_,salary,_ in Employee}
print("id to salary :- ",id_to_sal)

filter_emp = [(id,dep,sal,status) for id,dep,sal,status in Employee if status == "permanent"]
# filter_emp = [(id,dep,sal,status) for id,dep,sal,status in Employee if status == "permaneeent"]
print("filtered employee :- ",filter_emp)

revised_salaries = [ (id, dept, salary + (salary * (0.10 if status == "permanent" else 0.05)), status) for id, dept, salary, status in Employee ]

total_sal = {dep : sum(sal for _,d,sal,_ in Employee if d == dep) for _,dep,_,_ in Employee}
print("total sal per department :- ",total_sal)


