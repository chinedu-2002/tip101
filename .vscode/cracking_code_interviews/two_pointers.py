"""
The Problem Statement (Problem 27.4)
"Given a string s, return whether its letters form a palindrome ignoring punctuation, 
spaces, and casing."

Input: A string (e.g., "Bob wondered, 'Now, Bob?'")

Output: True or False
"""
#def is_palidrome(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if not s[left].isalpha():
#             left += 1
#         elif not s[right].isalpha():
#             right -= 1
#         else:
#             if s[left].lower() != s[right].lower():
#                 return False
#             left += 1
#             right -= 1
#     return True
# s = "Bob wondered, 'Now, Bob?'"
# print(is_palidrome(s))


"""
Given a sorted array of integers, arr, remove duplicates in place while 
preserving the order, and return the number of unique elements. 
It doesn't matter what remains in arr beyond the unique elements.


Example 1:
Input: arr = [1, 2, 2, 3, 3, 3, 5]
Output: 4
After the operation, the first 4 elements should be [1, 2, 3, 5]
The last 3 values could be anything

Example 2:
Input: arr = []
Output: 0
After the operation, the array remains empty

Example 3:
Input: arr = [1, 1, 1]
Output: 1
After the operation, the first element should be [1]
The last 2 values could be anything.
"""

# def remove_duplicates(nums):
#     left = 0
#     right = 0

#     while right < len(nums):
#         if right == 0 or nums[right] != nums[right - 1]:
#             nums[left] = nums[right]
#             left += 1
#         right += 1
#     return left
# arr = [1, 2, 2, 3, 3, 3, 5]
# print(remove_duplicates(arr))