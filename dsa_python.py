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

        while i < j:                            #--> same as that for range
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

        for i in range(n):   # starts from the 0 ,,,,,,,,,,,,,0 se n-1
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


"""
Valid Palindrome (Two pointer) HARD :- 
class Solution2 :
    def isAlpha(self,s,i):
        x = ord(s[i]) # function for calculating the ascii value

        if 97<=x<=122 or 48<=x<=57:
            return True
        else :
            return False

    def isPalindrome(self, s:str) -> bool:
        s = s.lower()
        n = len(s)
        i ,j = 0,n-1

        if not self.isAlpha(s,i):
            i+=1
            continue
        if not self.isAlpha(s,j):
            j+=1
            continue

        if s[i]==s[j]:
            i+=1
            j-=1
        else :
            return False

"""
# chars = ["h","e","l","l","o"]
# # Output → ["o","l","l","e","h"]

from typing import List

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         n = len(s)
#         i,j = 0,n-1

#         for i in range(n):
            
"""
✅ Q2. Remove Element (Two Pointer – like Move Zero)
👉 Remove all occurrences of val in-place.
nums = [3,2,2,3]
val = 3
Final array should contain only non-3 elements in front.
👉 Very similar to your MoveZero.
"""

print("\n\t [2, 2] \n\t")

from typing import List
class Solution:
    def remElement(self, nums: List[int], val: int) -> List[int]:
        # Use list comprehension for simplicity
        nums = [x for x in nums if x != val]
        return nums

s = Solution()
nums = [3, 2, 2, 3]
val = 3
result = s.remElement(nums, val)
print(result)   # Output: [2, 2]

print("\n\t Even Numbers front \n\t")

"""
✅ Q5. Move all even numbers to front (in-place)
nums = [1,2,3,4,5,6]
Result (order doesn't matter):
[2,4,6, ?, ?, ?]

"""

class Solution1 :
    def MoveEven(self, even:List[int]) -> List[int] :   # even = [1,2,3,4,5,6]
        n = len(even)
        i,j = 0,n-1
        start = 0
        for i in range(n):
            if even[i] % 2 == 0 :
                even[i],even[start] = even[start],even[i]
                start+=1

s1 = Solution1()    
even = [1,2,3,4,5,6]
s1.MoveEven(even)
print(even)


"""
✅ Q3. Squares of a Sorted Array (Two Pointer)
👉 Given a sorted array (can have negatives):
nums = [-4,-1,0,3,10]
Return:
[0,1,9,16,100]                          --------------------> Remaining
⚠️ But do it using
"""


print("\n\t [2,7] \n\t")

"""
👉 Two pointer + swap logic.
✅ Q6. Two Sum II – but return values, not indexes
(variation of your first code)
numbers = [2,7,11,15]
target = 9
Return:
[2,7]
Not indexes
"""

class Solution4:
    def addswap(self, numbers : List[int], target :int) -> List[int]:
        n = len(numbers)
        i,j = 0 ,n-1

        # for i in range is wrong here -> as it also increments the i here and you are also incrementing the i in the program
        while i < j :   # ex :- 0 < 4   
        
            s = numbers[i] + numbers[j]
            if s > target :
                j-=1
            elif s < target :
                i+=1
            else :
                return [numbers[i], numbers[j]]

s4 = Solution4()
numbers = [2,7,11,15]
target = 9
print(s4.addswap(numbers,target))

#======================================================================================================================================

"""
Find Pivot Index (Post prefix Method):- 
"""
class Pivot :
    def PiovotIndex(self, nums :List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0

        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum+=nums[i]
        return -1
    
pi = Pivot()
nums = [1,7,3,6,5,6]
print(pi.PiovotIndex(nums))

"""
Remove Duplicates from Sorted Array :- 
✅ Q2. Remove Duplicates from Sorted Array
nums = [1,1,2,2,3]
Make first part:
[1,2,3]
👉 return new length

class Remove:
    def RemoveDuplicate(self, nums :List[int]) -> List[int]:
        n = len(nums)
        # i,j = 0, n-1
        start = 0

        for i in range(n) :
            if 

"""

"""
Print Matrix in Spiral Order :- 
"""
