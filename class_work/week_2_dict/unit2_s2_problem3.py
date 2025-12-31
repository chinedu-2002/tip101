"""
Problem 1: Return Book
Write a function return_book() that accepts a string title and a dictionary 
library as parameters. library maps book titles to the number of copies the 
library currently has in stock. The function should increment the quantity of the 
book title in library by 1. If title is not in the library, then add it and set 
quantity to 1. Return the updated library dictionary.

def return_book(title, library):
    pass
Example Usage:

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)

Example Output:

{'The Hobbit': 2, '1984': 2, 'The Great Gatsby': 4}
{'The Hobbit': 2, '1984': 1, 'The Great Gatsby': 4, 'The Giver': 1}
"""
# def return_book(title, library):

#     if title not in library:
#         library[title] = 1
#     else:
#         library[title] += 1
#     return library


# library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

# updated_lib = return_book("1984", library)
# print(updated_lib)

# updated_lib = return_book("The Giver", library)
# print(updated_lib)



"""
Problem 2: Dictionary Difference
Write a function dict_difference() that takes two dictionaries and returns
a new dictionary that contains only the key-value pairs found only in the 
first dictionary but not in the second.

def dict_difference(d1, d2):
    pass
Example Input:

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d1, d2))
Example Output: {'a': 1, 'c': 3, 'd': 4}
"""
# def dict_difference(d1, d2):
#     new = {}
#     for key in d1:
#         if key not in d2:
#             new[key] = d1[key]
#         else:
#             if key in d2 and d1[key] != d2[key]:
#                 new[key] = d1[key]
#     return new
# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 2, 'd': 1}
# print(dict_difference(d1, d2))



"""
Problem 3: Take from Stock
Write a function pop_stock() that takes a dictionary of items items that 
keeps track of an item and its stock quantity, an item_name, and a quantity to be 
removed as parameters. The function should remove the specified quantity for that item.
If the item does not exist, return the string "Item does not exist."
If the specified quantity is greater than the stock, return a string "Not enough stock."
If the specified item and quantity do exist within items, decrement 
the item's stock by the specified quantity and return the updated dictionary.

def pop_stock(items, item_name, quantity):
    pass
Example Usage:

items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
print(resultB)
print(resultC)
print(resultD)
Example Output:

{'chocolate': 20, 'candy': 3, 'chips': 10}
Not enough stock
Item does not exist
{'chocolate': 15, 'candy': 3, 'chips': 10}
"""

# def pop_stock(items, item_name, quantity):
#     if item_name not in items:
#         return "Item does not exist."
#     if quantity > items[item_name]:
#         return "Not enough stock."
#     items[item_name] -= quantity
#     return items
# items = {"chocolate": 20, "candy": 5, "chips": 10}

# resultA = pop_stock(items, "candy", 2)
# resultB = pop_stock(items, "candy", 5)
# resultC = pop_stock(items, "lollipops", 5)
# resultD = pop_stock(items, "chocolate", 5)

# print(resultA)
# print(resultB)
# print(resultC)
# print(resultD)
            

"""
Problem 4: Group By Frequency
Write a function group_by_frequency() that takes in a list lst and returns a dictionary 
where keys represent the frequency of unique elements within lst and values 
represent a list of elements with the same frequency.

def group_by_frequency(lst):
    pass
Example Usage:

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))
Example Output:

{ 1 : ['a', 'b'], 2: ['c', 'd'], 3: ['e']}

"""

# def group_by_frequency(lst):
#     dict = {}

#     freq_str = {}

#     for num in lst:
#         dict[num] = dict.get(num, 0) + 1
    
#     for key, val in dict.items():
#         if val not in freq_str:
#             freq_str[val] = [key]
#         else:
#             freq_str[val].append(key)
#     return freq_str
# lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
# print(group_by_frequency(lst))
    

"""
Problem 5: No Duplicates Allowed
Write a function that takes in a list of integers nums as a parameter 
and removes all duplicates. The function should return a list containing 
the unique elements in the order of their last occurrence in the original list.

"""
# def remove_duplicates_from_front(nums):
#     last_index = {}
#     for i, num in enumerate(nums):
#         last_index[num] = i   
#     result = [num for num, idx in sorted(last_index.items(), key=lambda x: x[1])]
#     return result
# nums = [6,5,3,5,2,8,3]
# print(remove_duplicates_from_front(nums))

"""
Problem 6: First Repeating Element
Write a function find_min_index_of_repeating() that takes in an integer list nums 
as a parameter and returns the minimum index of an element that has a duplicate value. 
The function should only do a single traversal of the list. 
If there are no repeating elements, return None.

def find_min_index_of_repeating(nums):
    pass
Example Usage:

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))
Example Output:

1
None
3

"""
def find_min_index_of_repeating(nums):
    dict = {}
    min_index = None
    
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = i
        else:
            first_index = dict[nums[i]]
            if min_index is None:
                min_index = first_index
            else:
                min_index = min(min_index, first_index)
    return min_index
nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))
    


"""
Problem 7: Target Sum
Write a function two_sum() that takes in a list of integers nums 
and an integer target as parameters. The function should return the indices 
of the two numbers that add up to target. You may assume that each input 
would have exactly one solution and you may not use the same element twice. 
The function can return the indices in any order.

def two_sum(nums, target):
    pass
Example Input:

nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)

print(q_1)
print(q_2)
print(q_3)
Example Output:

[0,1]
[1,2]
[0,1]
"""
# def two_sum(nums, target):
#     dict = {}
    
#     for i in range(len(nums)):
#         target_sum = target - nums[i]
#         if target_sum in dict:
#             return [dict[target_sum], i]
#         dict[nums[i]] = i

# nums = [2,7,11,15]
# q_1 = two_sum(nums,9)
# q_2 = two_sum(nums,18)

# nums2 = [3,3]
# q_3 = two_sum(nums2,6)

# print(q_1)
# print(q_2)
# print(q_3)
