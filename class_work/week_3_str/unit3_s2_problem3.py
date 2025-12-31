"""
Problem 1: Remove Vowels
Write a function remove_vowels() that takes in a string s as a 
parameter and returns a new string with all the vowels removed. 
For the purposes of this exercise, consider a, e, i, o, and u as 
vowels and not y. The function should preserve the case of the
original letters.

def remove_vowels(s):
    pass
Example Usage:

s = "Hello World"
new_string = remove_vowels(s)
print(new_string)
Example Output: Hll Wrld
"""
# def remove_vowels(s):
#     vowels = set("aeiouAEIOU")
#     new = ""
#     for char in s:
#         if char not in vowels:
#             new += char
#     return new

# s = "Hello World"
# new_string = remove_vowels(s)
# print(new_string)

"""
Problem 2: Missing Integer
Write a function find_missing_positive() that takes in a sorted
list of integers nums that always starts at 1, and returns the 
smallest missing positive integer.

def find_missing_positive(nums):
    pass
Example Usage:

nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))
Example Output:

4
6
"""
# def find_missing_positive(nums):
#     for i in range(len(nums)):
#         if nums[i] != i + 1:
#             return i + 1
#     return len(nums) + 1
# nums1 = [1,2,3,5,6,10]
# print(find_missing_positive(nums1))

# nums2 = [1,2,3,4,5]
# print(find_missing_positive(nums2))
    


"""
Problem 3: Word Follows Pattern
Write a function wordPattern() that takes in a string pattern 
and a string s as parameters. The function returns True if s follows 
the pattern and False otherwise. The string follows the pattern 
if there is a 1:1 correspondence between a letter in the 
pattern and a non-empty word in s.

def wordPattern(pattern, s):
    pass
Example Usage:

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))

s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))
Example Output:

True
False
False
True

"""


"""
Problem 4: Binary Substrings
Write a function binary_substrings_count() that takes in a string s 
representing a binary number as a parameter. The function counts 
the number of substrings that satisfy all of the following conditions:

contains an equal number of 0s and 1s
all the 0s in the substring are grouped consecutively
all the 1s in the substrings are grouped consecutively
def binary_substrings_count(s):
    pass
Example Usage:

s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))
Example Output:

# substrings for s: "0011", "01", "1100", "10", "0011", "01"
6
# substrings for s2: "10", "01", "10", "01"
4
# substrings for s3: 
0
"""


"""
Problem 5: Exclusive Elements
Write a function exclusive_elements() that takes in two integer
lists lst1 and lst2 as parameters and returns a new list that 
contains the elements that are exclusively in one list only 
(elements that are in lst1 but not in lst2 and elements that are 
in lst2 but not in lst1)

def exclusive_elements(lst1, lst2):
    pass
Example Usage:

lst1 = [3,1,8,10]
lst2 = [4,5,3,7,8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)
Example Output: [1,10,4,5,7]


"""

"""
Problem 6: Flowerbed
Imagine you have a flowerbed in which some of the plots are planted, 
and some are not. Flowers cannot be planted in adjacent plots.

Write a function can_place_flowers() that takes in an integer list 
flowerbed containing 0's and 1's, (where 0 is an empty plot and 1 is a 
planted plot) and an integer n that represents the number of new flowers 
wanting to be planted as parameters. The function should return True 
if n new flowers can be planted in the flowerbed without violating 
the no-adjacent-flowers rule and False otherwise.

def can_place_flowers(flowerbed, n):
    pass
Example Usage:

flowerbed = [1,0,0,0,1]
approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)
print(approved)
print(approved2)
Example Output:

True
False

"""