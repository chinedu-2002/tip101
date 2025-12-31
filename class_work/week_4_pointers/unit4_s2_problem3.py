"""
Problem 1: Highest Exponent
Write a function find_highest_exponent() that takes in an integer base and 
an integer limit as parameters. The function returns the highest exponent 
for which a given base raised to that exponent is less than or equal to limit.

def find_highest_exponent(base, limit):
    pass
Example Usage:

exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)
Example Output:

# 2^6 = 64 and 2^7 = 128
6
# 3^1 = 3 and 3^2 = 9
1
"""

"""
Problem 2: Two-Pointer Target Sum
Write a function two_sum() that takes in a sorted list of integers nums 
and an integer target as parameters and returns the indices of the two numbers 
that add up to target. You may assume that each input would have exactly 
one solution, and you may not use the same element twice. You can 
return the indices in any order.

The function must use the two-pointer approach, which is a common technique 
in which we initialize two variables (also called a pointer in this context) 
to track different indices or places in a list or string, then moves the 
pointers to point at new indices based on certain conditions. In the most 
common variation of the two-pointer approach, we initialize one variable to 
point at the beginning of a list and a second variable/pointer to point at 
the end of list. We then shift the pointers to move inwards through the list 
towards each other, until our problem is solved or the pointers reach the 
opposite ends of the list.

def two_sum(nums, target):
    pass
Example Usage:

nums = [2,7,11,15,17]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)
Example Output

[0,1]
[1,2]

"""


"""
Problem 3: Evaluate Two Sum
The two_sum() problem can also be solved without using the two pointer technique
(as you may have seen it in previous units)! Evaluate the time and space complexity 
of your two-pointer solution.

Then, evaluate the time and space complexity of the following solution:

def two_sum(nums, target):
    prev_map = {}  # Value to index mapping
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i
Which has better time complexity?
Which has better space complexity?
"""


"""
Problem 4: Two-Pointer Reverse Letters
Using the two-pointer approach, write a function reverse_only_letters()
that takes in a string s as a parameter. The function reverses the order 
of the letters in the string and returns the new string. Non-letter characters 
should remain in their original positions.

def reverse_only_letters(s):
    pass
Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
Example Output: j-Ih-gfE-dCba
"""

"""
Problem 5: Reverse Prefix
Write a function reverse_prefix() that takes in a 0-indexed string word and 
a character ch as parameters. The function reverses the segment of word that 
starts at index 0 and ends at the index of the first occurrence of ch (inclusive) 
and keeps the rest of the string the same. If ch does not exist in word, do nothing. Return the resulting string.

def reverse_prefix(word, ch):
    pass
Example Usage:

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)
Example Output:

dcbaefd
wollehorld
xyzxyz
"""

"""
Problem 6: Squash Spaces
The two-pointer approach can also be used with two pointers that iterate forward 
through a list or string at different rates. Use two pointers to solve the following problem:

Write a function squash_spaces() that takes in a string s as a parameter and 
returns a new string with each substring with consecutive spaces reduced to a 
single space. Assume s can contain leading or trailing spaces, but in the result 
should be trimmed.

Do not use any of the built-in trim methods.

def squash_spaces(s):
    pass
Example Usage:

print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))
Example Output:

hello world
what about this ?
this is my sentence
"""