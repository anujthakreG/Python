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
Print Matrix in Spiral Order :-   ------> remaining
"""

# calculating the frequency :
list1 = [2,3,4,1,2,3,4,5,4,3,2]
freq = {}

for i in list1:
    if i in freq:
        freq[i] += 1
    else :
        freq[i] = 1

for i in freq:
    print(F" {i} is present {freq[i]} times")


"""
Sorted Array -> Two pointer can be used coz we know the target value acc to that we can shift the right/left pointer 
Tow Sum :- Array is Unsorted -> Hashing 
"""


print("\n\t Sliding Widow problems \n\t")

# Sliding Widow problems :- 
# calculating the max avg of sub array :- 

class Window1 :
    def avgsub(self,nums : List[int], k: int) -> int:
        n = len(nums)
        curr_sum = 0

        for i in range(n):
            curr_sum+= nums[i]
        
        ans = curr_sum  / k

        for i in range(k,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            ans = max(ans,curr_sum / k)

        return ans
w = Window1()
nums = [1,12,-5,-6,50,3]
print(w.avgsub(nums,4))

"""
✅ Q9. Longest substring without repeating characters                     # LC-> 3
(Sliding window – variable size)
s = "abcabcbb"
"""

class Substring :
    def longString(self, s :str)  -> int:
        n = len(s)
        if n <= 1 :
            return n
        
        i , j = 0 , 1
        set1 = set({})
        set1.add(s[0])
        ans = 1

        while j < n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            
            set1.add(s[j])
            j+=1
            ans = max(ans,(j-i))
        return ans

st = Substring()
s = "abcadbac"
print(st.longString(s))


"""
Kadane's Algorithm :- 
Maximium Subarray :- LC ->> 53 
"""

# class Kadane:
#     def maxSubarray(self, nums : List[int]) -> List[int] :

# repeat 
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
Print Matrix in Spiral Order :-   ------> remaining
"""

# calculating the frequency :
list1 = [2,3,4,1,2,3,4,5,4,3,2]
freq = {}

for i in list1:
    if i in freq:
        freq[i] += 1
    else :
        freq[i] = 1

for i in freq:
    print(F" {i} is present {freq[i]} times")


"""
Sorted Array -> Two pointer can be used coz we know the target value acc to that we can shift the right/left pointer 
Tow Sum :- Array is Unsorted -> Hashing 
"""


print("\n\t Sliding Widow problems \n\t")

# Sliding Widow problems :- 
# calculating the max avg of sub array :- 

class Window1 :
    def avgsub(self,nums : List[int], k: int) -> int:
        n = len(nums)
        curr_sum = 0

        for i in range(n):
            curr_sum+= nums[i]
        
        ans = curr_sum  / k

        for i in range(k,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            ans = max(ans,curr_sum / k)

        return ans
w = Window1()
nums = [1,12,-5,-6,50,3]
print(w.avgsub(nums,4))
