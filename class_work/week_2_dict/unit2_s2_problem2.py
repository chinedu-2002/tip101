"""
Problem 1: Update Score
Write a function update_score() that takes in a dictionary scores that maps player names to 
current scores, a string player, and an integer points as parameters. 
The function adds the points to the current score of player in the dictionary and
returns the updated dictionary. 
If the player does not exist in scores, then add them.

def update_score(scores, players, points):
    pass
Example Usage:

scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
update_score(scores, "Calvin", 20)
print(scores)
update_score(scores, "Calvin", 5)
print(scores)
Example Output:

{'Alice': 110, 'Bob': 90}
{'Alice': 110, 'Bob': 90, 'Calvin': 20}
{'Alice': 110, 'Bob': 90, 'Calvin': 25}
"""
# def update_score(scores, players, points):
#     if players in scores:
#         scores[players] += points
#     else:
#         scores[players] = points
# scores = {"Alice": 100, "Bob": 90}
# update_score(scores, "Alice", 10)
# print(scores)
# update_score(scores, "Calvin", 20)
# print(scores)
# update_score(scores, "Calvin", 5)
# print(scores)


"""
Problem 2: Dictionary Intersection
Write a function dict_intersection() that takes in two dictionaries as 
parameters and returns a new dictionary containing the key-value pairs 
found in both dictionaries.

def dict_intersection(d1, d2):
    pass
Example Input:

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
Example Output: {'b': 2}
"""

# def dict_intersection(d1, d2):
#     dict = {}

#     for key in d1:
#         if key in d2 and d1[key] == d2[key]:
#             dict[key] = d1[key]
#     return dict

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 4}
# print(dict_intersection(d1, d2))
# def dict_intersection(d1, d2):
#     dict = {}
#     for key, val in d1.items():
#         if key in d2 and val == d2[key]:
#             dict[key] = val
#     return dict
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 4}
# print(dict_intersection(d1, d2))

"""
Problem 3: Filter by Price
Write a function that takes in a dictionary of items and a price_threshold 
as parameters. The function should iterate through the dictionary 
and remove all items that has a  value less than price_threshold. 
The function also returns a list of all items that are removed. 
If no item satisfies the condition, return None.

def remove_items_below_price(items, price_threshold):
    pass
Example Usage:

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)
Example Output:

["banana", "date"]
None
"""
# def remove_items_below_price(items, price_threshold):
#     new = []

#     for key in items:
#         if items[key] < price_threshold:
#             new.append(key)
#             #items.pop(key)
#     for key in new:
#         items.pop(key)
#     return new if new else None
# items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
# removed_list = remove_items_below_price(items, 1.00)
# print(removed_list)
# removed_list_two = remove_items_below_price(items, 1.00)
# print(removed_list_two)


"""
Problem 4: Find Odd Occurrences
Write a function find_odd_occurrences() that takes in a list of integers numbers
where all numbers occur an even number of times except for two unique numbers
that occur an odd number of times. The function should find the two unique numbers 
and return them as a list. Assume each problem has exactly one solution.

def find_odd_occurrences(numbers):
    pass
Example Usage:

numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)
Example Output:

[1,3]
"""
# def find_odd_occurrences(numbers):
#     dict = {}
#     for key in numbers:
#         dict[key] = dict.get(key, 0) + 1
#     new = []
#     for key in dict:
#         if dict[key] % 2 == 1:
#             new.append(key)
#     return new
# numbers = [1,4,2,3,2,3,3,4,4,4]
# odd_list = find_odd_occurrences(numbers)
# print(odd_list)


"""
Problem 5: Find Mode
Write a function find_mode() that takes in a non-empty list of integers lst 
as a parameter. The function returns the mode (the most frequently occurring 
number) and if there is a tie, return the element which appeared first 
in the list.

def find_mode(lst):
    pass
Example Usage:

lst = [1,2,3,2,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)
Example Output: 4
"""
# def find_mode(lst):
#     dict_freq = {}
#     dict_occuring = {}

#     for i,val in enumerate(lst):
#         dict_freq[val] = dict_freq.get(val, 0) + 1
#         if val not in dict_occuring:
#             dict_occuring[val] = i

#     highest_freq = float('-inf')
#     highest_num = list(dict_freq.keys())[0]

#     for val in dict_freq:
#         if dict_freq[val] > highest_freq or (dict_freq[val] == highest_freq and dict_occuring[val] < dict_occuring[highest_num]):
#             highest_freq = dict_freq[val]
#             highest_num = val
#     return highest_num
# lst = [1,2,3,2,3,3,4,4,4,4]
# mode = find_mode(lst)
# print(mode)


"""
Problem 6: How Many Smaller
Write a function smaller_numbers_than_current() that takes in a list of 
numbers nums as a parameter. For each nums[i], the function should 
find out how many numbers in the list are smaller than it. 
(For each nums[i], count the number of valid j's such that j!=i 
and nums[j] < nums[i])

Return the answers in a list.

def smaller_numbers_than_current(nums):
    pass
Example Input:

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))
Example Output: [4,0,1,1,3]

Explanation:

nums[0] == 6
There exists four smaller numbers than it (1, 2, 2 and 3) --> ans[0]=4

nums[1] == 1 
There does not exist any smaller number than it --> ans[1]=0

nums[2] == 2 
There exists one smaller number than it (1) --> ans[2]=1

nums[3] == 2 
There exists one smaller number than it (1) --> ans[3]=1

nums[4] == 3 
There exists three smaller numbers than it (1, 2 and 2) --> ans[4]=3

"""
# def smaller_numbers_than_current(nums):
#     dict = {}

#     for num in nums:
#         dict[num] = dict.get(num, 0) + 1
    
#     sorted_num = sorted(dict.keys())

#     prefix = {}
#     total = 0
#     for num in sorted_num:
#         total += dict[num]
#         prefix[num] = total

#     res = []
#     for num in nums:
#         count = prefix[num] - dict[num]
#         res.append(count)
#     return res
# nums = [6,1,2,2,3]
# print(smaller_numbers_than_current(nums))

# def smaller_numbers_than_current(nums):
#     sorted_num = sorted(nums)
#     dict = {}
    
#     for i in range(len(sorted_num)):
#         if sorted_num[i] not in dict:
#             dict[sorted_num[i]] = i
    
#     res = []
#     for num in nums:
#         if num in dict:
#             res.append(dict[num])
#     return res
# nums = [6,1,2,2,3]
# print(smaller_numbers_than_current(nums))
        


"""
Problem 7: Good Pairs
Write a function num_identical_pairs() that takes in a list of integers nums 
and returns the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def num_identical_pairs(nums):
    pass
Example 1:

nums = [1,2,3,1,1,3]
print(num_identical_pairs(nums))

nums = [1,2,3]
print(num_identical_pairs(nums))

nums = [1,1,1,1]
print(num_identical_pairs(nums))
Example Output:

4
0
6
Example 1 Explanation:

nums[0] == 1
- nums[0] == nums[3]
- nums[0] == nums[4]
Good Pairs: (0,3) and (0,4) --> count = 2

nums[1] == 2
No identical pairs found

nums[2] == 3
- nums[2] == nums[5]
Good Pairs: (2,5) --> count = 3

nums[3] == 1
*will not check any any indices less than current index*
- nums[3] == nums[4]
Good Pairs: (3,4) --> count = 4

nums[4] == 1
*will not check any any indices less than current index*
No identical pairs found

nums[5] == 3
*will not check any any indices less than current index*
No identical pairs found
"""


# def num_identical_pairs(nums):
#     dict = {}

#     for num in nums:
#         dict[num] = dict.get(num, 0) + 1
    
#     pairs = 0
#     for num in dict.values():
#         pairs += num * (num - 1) // 2
#     return pairs
# nums = [1,2,3,1,1,3]
# print(num_identical_pairs(nums))

# nums = [1,2,3]
# print(num_identical_pairs(nums))

# nums = [1,1,1,1]
# print(num_identical_pairs(nums))
