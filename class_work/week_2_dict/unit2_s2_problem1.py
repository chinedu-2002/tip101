"""
Problem 1: Cast Vote
Write a function cast_vote() that records a vote for a candidate in an election. 
The function accepts a dictionary votes that maps candidates to their 
current number of votes and a string candidate that represents 
the candidate the user would like to vote for. 
If the candidate doesn't exist, add them to the dictionary. 
The function should return the updated dictionary.

def cast_vote(votes, candidate):
    pass
Example Usage:

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
Example Output:

{'Alice': 6, 'Bob': 3}
{'Alice': 6, 'Bob': 3, 'Gina': 1}
"""

# def cast_vote(votes, candidate):
#     if candidate in votes:
#         votes[candidate] += 1
#     else:
#         votes[candidate] = 1
# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)



"""
Problem 2: Keys in Common
Write a function that takes in two dictionaries, dict1 and dict2 and 
finds all keys common to both dictionaries. The function returns a 
list of common keys.

def common_keys(dict1, dict2):
	pass
Example Usage:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
Example Output:

['b', 'c']
"""
# def common_keys(dict1, dict2):
#     new = []

#     for key in dict1:
#         if key in dict2:
#             new.append(key)
#     return new
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)

"""
Problem 3: Frequency Count
Write a function that takes in a list of integers nums 
and counts the number of occurrences of each integer. 
The function returns the result as a dictionary with 
integers as keys and their counts as values.

def count_occurrences(nums):
    pass
Example Input: nums = [1, 2, 2, 3, 3, 3, 4]
Example Output: {1: 1, 2: 2, 3: 3, 4: 1}
"""
# def count_occurrences(nums):
#     mapping = {}

#     for val in nums:
#         mapping[val] = mapping.get(val, 0) + 1
#     return mapping
# nums = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums))

"""
Problem 4: Highest Priority Task
Given a dictionary tasks where keys are task names 
and values are priorities (1-10, where 10 is the highest priority), 
write a function get_highest_priority_task() 
that removes the task with the highest priority from the dictionary 
and returns its name.
If two tasks have the same priority, return 
the task that comes first in the alphabet.

def get_highest_priority_task(tasks):
	pass
Example Usage:

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
Example Output:

task2
task4
task3
{'task1': 8,'task5': 7}
"""
# def get_highest_priority_task(tasks):
#     highest_rating = float('-inf')
#     task_name = None
    
#     for key in tasks:
#         if tasks[key] > highest_rating:
#             highest_rating = tasks[key]
#             task_name = key
#         elif tasks[key] == highest_rating and key < task_name:
#             task_name = key
#     tasks.pop(task_name)
#     return task_name
# tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# print(tasks)

"""
Problem 5: Find Majority Element
Write a function find_majority_element() that takes in a list of integers 
elements and finds the majority element in the list. 
A majority element is an element that appears more than 
n/2 times where n is the size of the list. If there is no majority element, return None.

def find_majority_element(elements):
    pass
Example Usage:

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
Example Output: 2
"""
# def find_majority_element(elements):
#     half = len(elements) / 2
#     dict = {}

#     for key in elements:
#         dict[key] = dict.get(key, 0) + 1
    
#     for key in dict:
#         if dict[key] > half:
#             return key
# elements = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements))
    

"""
Problem 6: Has Duplicates
Write a function has_duplicates() that takes in a list of integers nums 
and a positive number k as parameters. 
The function returns True if the list contains any duplicate elements 
within k (inclusive) indices of each other. 
In other words, return True if nums[i] has the same value as any of 
the k neighboring elements to its left or right. If k is greater than the list's length, 
the solution should check for duplicates in the complete list. 
The function should return False otherwise.

def has_duplicates(nums, k):
	pass
Example Usage:

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 2)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)
check3 = has_duplicates(nums, 3)
print(check3)
Example Output:

False
True
True
"""

# def has_duplicates(nums, k):
#     dict = {}

#     for key in range(len(nums)):
#         if nums[key] not in dict:
#             dict[nums[key]] = key
        
#         else:
#             if nums[key] in dict:
#                 if key - dict[nums[key]]  <= k:
#                     return True
#                 else:
#                     return False
# nums = [5, 6, 8, 2, 6, 4, 9]
# check1 = has_duplicates(nums, 2)
# print(check1)
# check2 = has_duplicates(nums, 5)
# print(check2)
# check3 = has_duplicates(nums, 3)
# print(check3)


"""
Problem 7: Make Pairs
Write a function divide_list() that takes in an integer list nums consisting of 
2*n integers as parameters. The function divides nums into n pairs such that:

Each element belongs to exactly one pair
The elements present in a pair are equal
Return True if nums can be divided into n pairs, otherwise return False.

def divide_list(nums):
    pass
Example Input:

nums = [3,2,3,2,2,2]
print(divide_list(nums))
Example Output: True
Explanation: There are 6 elements in nums, so they should be 
divided into 6 / 2 = 3 pairs. 
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy
all the conditions.

Example Input:

nums = [1,2,3,4]
print(divide_list(nums))
Example Output: False
Explanation: There is no way to divide nums into 4 / 2 = 2 pairs 
such that the pairs satisfy every condition.

"""

def divide_list(nums):
    dict = {}

    for key in nums:
        dict[key] = dict.get(key, 0) + 1
    for key in dict:
        if dict[key] % 2 != 0:
            return False
        
    return True
nums = [1,2,3,4]
print(divide_list(nums))
nums = [3,2,3,2,2,2]
print(divide_list(nums))

