"""
Docstring for dsa_python
starting the dsa concepts in the respective order :- 
Order for doing Dsa :- 

1️⃣ Arrays / Lists
2️⃣ Strings
3️⃣ Recursion
4️⃣ Searching (Linear, Binary)
5️⃣ Sorting (Bubble, Selection, Merge)
6️⃣ Stack
7️⃣ Queue
8️⃣ Linked List
9️⃣ Hashing
🔟 Trees & Graphs (later)

"""

"""
1> Time Complexity :- it describes the execution time of an algorithm as the input size increases 
all the notations -> remaining 
Asymptotic notation is similar to unit of measurment of time complexity

  NUMBER OF OPERATIONS = TIME COMPLEXITY 

=> linear time (O(n)) -> No. of inputs = No. of operations
      ex :- n = input()
            for i in range(n):    or n + c {c -> constant }
               print(i)

=> constant time (O(1)) -> here program does not perform any of the operations 
=> Quadratic (O(n^2))  -> perhaps a nested loop
     ex :- for i in range(n):  {n^2}
             for j in range(n) :   
                print(i)         --> if O(n^2 + n)  == O(n^2)  they are same

=> Exponential -> recurrssion 
=> Linearathmic (O(n logn))
"""


""" 
=> logarithmic Time (O(Log n))
"""
# O(logn2n)  base = 2
n = 100
i = 1

while i<= n:  # assuming the loop runs k times 
    # print(i, end= " ")
    i*=2   # 1,2,2^2,2^33  ....... 2^k , will stop when 2^k = n 


"""
General idea: (We Know)
List -> Ordered , Mutable(can be chnaged) , Allow Duplicates

"""

"""
Two Pointers (Whenever we have to compare any condition of two numbers/Index we use it )
"""

# Two sum (Sorted Array)
from typing import List
class Solution :
    def twoSum(self, numbers : List[int], target : int) -> List[int]:   # target : 41
        n = len(numbers)
        i,j = 0,n-1

        while i < j:
            s = numbers[i] + numbers[j]
            if s > target :
                j-=1
            elif s < target :
                i+=1 
            else :
                return  [i+1,j+1]  # to take the output form 1 
        return [-1,-1]
            
s = Solution() 
numbers = [2, 7, 11, 15] 
target = 9 
print(s.twoSum(numbers, target))

# Move Zeroes :- 
class MoveZero :
    def move(self, nums : List[int]) -> None:
        # we have to keep two pointers start and i 
        start = 0  # start is for keeping 
        n = len(nums)

        for i in range(n):   # starts from the 0 
            if nums[i] !=0 :
                # swap it if it is non zero element 
                nums[i], nums[start] = nums[start], nums[i]
                start+=1
            # return []
m1 = MoveZero()
nums = [0,1,0,3,12]
# nums = [1,2,0,3,12]
# print(m1.move(nums))   -> was not working
m1.move(nums)
print(nums)

"""
#  when to buy and sell stock ques remaining 
class Solution1 :
    def maxProfit(self, prices : List[int]) -> int:
        n = len(prices)
        min_profit = prices[0]
        ans = 0

        for i in range(1,n) :  # coz we are considering buying on day 1 i.e prices[o]
            curr_profit = prices[i] - min_profit
            curr_profit = max()
"""


# Valid Palindrome (Two pointer) HARD :- 
# class Solution2 :
#     def isAlpha(self,s,i):
#         x = ord(s[i]) # function for calculating the ascii value

#         if 97<=x<=122 or 48<=x<=57:
#             return True
#         else :
#             return False

#     def isPalindrome(self, s:str) -> bool:
#         s = s.lower()
#         n = len(s)
#         i ,j = 0,n-1

#         if not self.isAlpha(s,i):
#             i+=1
#             continue
#         if not self.isAlpha(s,j):
#             j+=1
#             continue

#         if s[i]==s[j]:
#             i+=1
#             j-=1
#         else :
#             return False
