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


#-------------------------------------------------------------------------------------------------------


"""
✅ Q1. Remove Duplicates from Sorted Array
(Two pointer)
nums = [1,1,2,2,3]
Make it:
[1,2,3, ...]
👉 In-place
👉 Return new length
"""

# class Second1:
#     def remDuplicates(self,nums: List[int]) -> List[int]:
#         n = len(nums)
#         i,j = 0, n-1
#         start = 0

#         for i in range(1,n-1):
#             if nums[start] == nums[i]:
#                 nums.remove(i)
#                 start+=1
            

print("\n\t Second shots \n\t")


"""
✅ Q2. Remove Element
(Two pointer – front pointer)
nums = [0,1,2,2,3,0,4,2]
val = 2
Remove all 2’s in-place.
"""

class Second2:
    def remelement(self,nums : List[int], val :int) -> int:
        n = len(nums)
        start = 0

        # nums = [0,1,2,2,3,0,4,2] 
        # val = 2  
        """   ------> wrong code remove always removes the value , but we want to remove the index element , we are removing the element at the time of loop (big bug)
        for i in range(n): 
            if nums[i] == val:
                nums.remove(i)
        return nums
        """
        for i in range(n):
            if nums[i] != val:
                nums[start] = nums[i]  # nums[start] updates the list nothing else
                start+=1
        return start   # function is returning new length not the list 

h = Second2()

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

new_len = h.remelement(nums, val)

print("New length:", new_len)
print("Final array (valid part):", nums[:new_len])  # this is how you get list 

"""
✅ Q3. Reverse Vowels of a String
(Two pointer + skip logic)
s = "hello"
Output:
"holle"
👉 Only vowels ko swap karna.

"""
class Second3:
    def reverseVowel(self, s: str) -> str:

        s = list(s)   # string immutable hota hai, so list banate hain

        vowels = set("aeiouAEIOU")

        i = 0
        j = len(s) - 1

        while i < j:

            # skip non-vowels from left
            if s[i] not in vowels:
                i += 1
                continue

            # skip non-vowels from right
            if s[j] not in vowels:
                j -= 1
                continue

            # both are vowels → swap
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)


# ---- test ----
h = Second3()
print(h.reverseVowel("hello"))

  
"""
✅ Q5. Sort Array by Parity
(Two pointer)
nums = [3,1,2,4]
Even first, odd later.
"""
class Second4:
    def sortarray(self,nums : List[int]) -> List[int]:
        n = len(nums)
        start = 0

        for i in range(n):
            if nums[i] % 2 == 0:
                nums[start],nums[i] = nums[i],nums[start]
                start+=1
        return nums
h4 = Second4()
nums = [3,1,2,4]
# h4.sortarray(nums)
print(h4.sortarray(nums))

"""
✅ Q6. Valid Palindrome – easy version
(Two pointer + skip)
s = "race a car"
Ignore spaces and case.
"""
class Second5:
    def validP(self,s :str) ->bool:
        n = len(s)
        i,j = 0,n-1

        while i < j:
            if s[i] == " ":
                i+=1
                continue
            if s[j] == " ":
                j-=1
                continue

            if s[i]==s[j]:
                i+=1
                j-=1
            else :
                return False
            

case = Second5()
s = "race a car"
print(case.validP(s))

#======================================================================================================================================


"""
Q8. Reverse Only Letters
s = "a-bC-dEf-ghIj"
"j-Ih-gfE-dCba"
"""
class Reverse :
    def fucn(self,s :str) -> bool:
        s = list(s)
        n = len(s)
        start = 0
        i,j = 0 ,n-1
        while i < j :
            if s[i] == "-":
                i+=1
                continue
            if s[j] == "-":
                j-=1
                continue
            else :
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        return "".join(s)

rev = Reverse()
s = "a-bC-dEf-ghIj"
print("input :- ",s)

print("Output :- ",rev.fucn(s))

"""
✅ Q10. Move All Negative Numbers to Left
nums = [1,-2,3,-4,5]
"""

class MoveNegative:
    def doing(self,nums :List[int]) -> List[int]:
        n = len(nums)
        start = 0


        for i in range(n):
            if nums[i] < 0:
                nums[start],nums[i] = nums[i],nums[start]
                start=+1
        return nums
mh = MoveNegative()
nums = [1,-2,3,-4,5]
print(mh.doing(nums))

"""
✅ Q6. Container With Most Water ⭐⭐⭐                ------> remaining
height = [1,8,6,2,5,4,8,3,7]
Return maximum area.
👉 left / right decision problem
"""

# class Container:
#     def MoveWater(self,height : List[int]) -> int:
#         n = len(height)

#======================================================================================================================================
                                                        #    Sliding Window Problem


"""
✅ Q7. Container With Most Water
(Two pointer – left / right logic)
height = [1,8,6,2,5,4,8,3,7]
Find max area.
⚠️ Very famous interview question.
"""



"""
✅ Q8. Subarray of size k with maximum sum
(Sliding window – fixed size)
nums = [2,1,5,1,3,2]
k = 3
"""




"""
✅ Q9. Longest substring without repeating characters
(Sliding window – variable size)
s = "abcabcbb"
"""



"""
✅ Q10. Minimum size subarray sum
(Sliding window – variable size)
nums = [2,3,1,2,4,3]
target = 7
"""
