"""
Problem 1: Perfect Number
Write a function is_perfect_number() that takes in a positive integer n 
and returns True if it is a perfect number and False otherwise. 
A perfect number is a positive integer that is equal to the sum of 
its proper divisors, excluding itself.

For example, 6 is a perfect number because its divisors or 1, 2, 
and 3 and 1 + 2 + 3 = 6.

def is_perfect_number(n):
    pass
Example Usage:

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))
Example Output:

True
True
False
"""

"""
Problem 2: 2-Pointer Palindrome
Write a function is_palindrome() that takes in a string s as a 
parameter and returns True if the string is a palindrome and False otherwise. 
You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach, which is a common technique 
in which we initialize two variables (also called a pointer in this context) 
to track different indices or places in a list or string, then moves 
the pointers to point at new indices based on certain conditions. 
In the most common variation of the two-pointer approach, we initialize 
one variable to point at the beginning of a list and a second 
variable/pointer to point at the end of list. We then shift the pointers 
to move inwards through the list towards each other, until our problem is 
solved or the pointers reach the opposite ends of the list.

def is_palindrome(s):
    pass
Example Usage:

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))
Example Output:

True
False
"""

"""
Problem 3: Evaluate Palindrome
The is_palindrome() problem can also be solved without using the 
two-pointer technique (as you may have seen it in previous units)! 
Evaluate the time and space complexity of your two-pointer solution.

Then, evaluate the time and space complexity of the following solution:

def is_palindrome(s):
    reverse = s[::-1]
    return reverse == s
Which has better time complexity?
Which has better space complexity?
"""


"""
Problem 4: Make Palindromes
You are given a string s consisting of lowercase English letters, 
and are allowed to perform operations on it. In one operation, 
you can replace a character in s with another lowercase English letter.

Write a function make_palindrome() that takes in a string s and turns 
it into a palindrome with the minimum number of operations as possible. 
If there are multiple palindromes that can be made using the minimum number
of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) 
if in the first position where a and b differ, string a has a letter that
appears earlier in the alphabet than the corresponding letter in b.

The function returns the resulting palindrome string.

def make_palindrome(s):
    pass
Example 1:

s = "egcfe"
print(make_palindrome(s))
# s_pal == "efcfe"
# The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# another palindrome possible is "egcge", but it is not lexicographically smaller
Example 2:

s = "abcd"
print(make_palindrome(s))
# s_pal == "abba"
# The min number of operations to make s a palindrome is 2 by changing `c` to `b` 
# and `d` to `a`
# a palindrome cannot be created in 1 operation
Example 3:

s = "seven"
print(make_palindrome(s))
# s_pal == "neven"
# The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# to get a palindrome that is lexographically smaller, it would take more operations
"""

"""
Problem 5: Reverse Vowels
Write a function reverse_vowels() that takes in a string s as a parameter 
and returns a string with all the vowels in the string reversed. 
The consonants should remain in the same position. For this question, 
we consider a, e, i, o, and u as vowels but not y. The vowels can appear 
in both lower and upper cases, more than once.

def reverse_vowels(s):
    pass
Example Usage:

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)
Example Output:

holle
leotcede
"""

"""
Problem 6: Two-Pointer Remove Element
The two-pointer approach can also be used with two pointers that iterate forward
through a list or string at different rates. Use two pointers to solve the following problem:

Write a function remove_element() that takes in a list nums and a value val
as parameters and removes all instances of that value in-place. The function
returns the new length of nums.

def remove_element(nums, val):
    pass
Example Usage:

nums = [5, 4, 4, 3, 4, 1]
nums_len = remove_element(nums, 4)
print(nums) # same list
print(nums_len)
Example Output:

[5, 3, 1]
3

"""