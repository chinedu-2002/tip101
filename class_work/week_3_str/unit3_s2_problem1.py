"""
Problem 1: Sum of Strings
Write a function sum_of_number_strings() that takes in a list of strings
nums. Each string is a representations of integers. 
The function should return the sum of these strings as an integer.

def sum_of_number_strings(nums):
    pass
Example Usage:

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
Example Output: 60
"""

# def sum_of_number_strings(nums):
#     total = 0
    
#     for num in nums:
#         total += int(num)
#     return total
# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)

"""
Problem 2: Remove Duplicates
Write a function remove_duplicates() that takes in a sorted list of 
integers nums as a parameter and removes all duplicates in the list. 
The function returns the modified list.

def remove_duplicates(nums):
    pass
Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
Example Output: no_dups = [1,2,3,4,5,6]
"""
# def remove_duplicates(nums):
#     left = 1
    
#     for right in range(1, len(nums)):
#         if nums[right] != nums[left - 1]:
#             nums[left] = nums[right]
#             left += 1
#     del nums[left:]        
#     return nums
# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))


"""
Problem 3: Reverse Letters
Write a function reverse_only_letters() that takes in a 
string s as a parameter. The function reverses the order of 
the letters in the string and returns the new string. 
Non-letter characters should remain in their original positions.

def reverse_only_letters(s):
    pass
Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
Example Output: j-Ih-gfE-dCba
"""
# def reverse_only_letters(s):
#     if not s:
#         return ""
#     chars = list(s)
#     left = 0
#     right = len(chars) - 1
    
#     while left < right:
#         if not chars[left].isalpha():
#             left += 1
        
#         elif not chars[right].isalpha():
#             right -= 1
#         else:
#             chars[left], chars[right] = chars[right], chars[left]
#             left += 1
#             right -= 1
#     return "".join(chars)

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)

"""
Problem 4: Longest Uniform Substring
Write a function longest_uniform_substring() that takes in a string s and returns the 
length of the longest uniform substring. A uniform substring consists of a single 
repeated character.

def longest_uniform_substring(s):
    pass
Example Usage:

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)
Example Output:

4
1

"""
# def longest_uniform_substring(s):
#     unqiue = s[0]
#     count = 1
#     max_num = float('-inf')
    
#     for i in range(1, len(s)):
#         if s[i] == unqiue:
#             count += 1
#         else:
#             max_num = max(max_num, count)
#             unqiue = s[i]
#             count = 1
#     return max_num
# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)


"""
Problem 5: Teemo's Attack
In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. 
Write a function find_poisoned_duration() that takes in two parameters: 
time_series (the time at which Teemo's attacks hits Ashe) and time_duration 
(the duration of the poisoning effect). The function returns the total time that 
Ashe is in a poisoned condition.

time_series is a list of integers that represents the times at which 
Teemo attacks and makes Ashe poisoned for the exact time_duration.

If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. 
For example, if Teemo attacks at times 1 and 4 for 3 seconds, the states at each time would be:

1: attacked
2: in poison state
3: in poison state
4: attacked, poison duration resets to 3
5: in poison state
6: in poison state
7: in poison state 
8: in normal state
This means that the total time that Ashe is in a poisoned condition is 5.

def find_poisoned_duration(time_series, duration):
    pass
Example Usage:

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)
Example Output: 8

"""

# def find_poisoned_duration(time_series, duration):
#     total_poison = 0
#     for i in range(len(time_series) - 1):
#         total_poison += min((time_series[i + 1] - time_series[i]) - 1, duration)
#     total_poison += duration
#     return total_poison
# time_series = [1,4,9]
# damage = find_poisoned_duration(time_series, 3)
# print(damage)


"""
Write a function sum_of_unique_elements() that takes in two lists of integers, 
lst1 and lst2, as parameters and returns the sum of the elements that are unique in lst1.

An element is unique if:

it appears exactly once in lst1
it does not appear in lst2
def sum_of_unique_elements(lst1, lst2):
	pass
Example Usage:

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)
Example Output

3
0

"""

# def sum_of_unique_elements(lst1, lst2):
#     dict = {}
    
#     for n in lst1 + lst2:
#         if n not in dict:
#             dict[n] = 0
#         dict[n] += 1
    
#     sum_total = 0    
#     for n in lst1:
#         if dict[n] == 1:
#             sum_total += n
#     return sum_total
            
            

# lstA = [1, 2 ,3, 4] 
# lstB = [3, 4, 5, 6]
# lstC = [7, 7, 7, 7]

# sum1 = sum_of_unique_elements(lstA, lstB)
# print(sum1)

# sum2 = sum_of_unique_elements(lstC, lstB)
# print(sum2)

            

            

        