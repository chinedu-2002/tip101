"""
Problem Set Version 1
Problem 1: All In
Write a function all_in() that takes in a list of integers a 
and a list of integers b as parameters. Given these two lists, 
return True if every element in list a is in list b. Return False otherwise.

def all_in(a, b):
    pass
Example Usage:

lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))
Example Output:

True
False
"""

# def all_in(a, b):
#     for n in a:
#         if n not in b:
#             return False
#     return True
# lst_1 = [1, 2]
# lst_2 = [1, 2, 3]
# print(all_in(lst_1, lst_2))
# print(all_in(lst_2, lst_1))


"""
Problem 2: Create a Dictionary
Write a function create_dictionary() that takes in a list of keys 
and a list of values as parameters. The function returns a dictionary 
where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). 
You may assume keys and values are the same length.

def create_dictionary(keys, values):
    pass
Example Input:

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
Example Output:

{'peanut': 'butter', 'dragon': 'fly', 'star': 'fish', 'pop': 'corn', 'space': 'ship'}
"""

# def create_dictionary(keys, values):
#     d = {}
    
#     for i in range(len(keys)):
#         d[keys[i]] = values[i]
#     return d
# keys = ['peanut', 'dragon', 'star', 'pop', 'space']
# values = ['butter', 'fly', 'fish', 'corn', 'ship']
# print(create_dictionary(keys, values))

"""
Problem 3: Print Pair
Write a function print_pair() that takes in a dictionary dictionary 
and a key target as parameters. The function looks for the target and when found, 
it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". 
If target is not in dictionary, print "That pair does not exist!".

def print_pair(dictionary, target):
    pass
Example Usage:

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
Example Output:

Key: patrick
Value: star
That pair does not exist!
Key: spongebob
Value: squarepants
"""
# def print_pair(dictionary, target):
#         if target in dictionary:
#             print(f"Key: {target}")
#             print(f"Value: {dictionary[target]}")
#         else:
#             print("That pair does not exist!")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")
            
"""
Problem 4: Keys Versus Values
Write a function keys_v_values() that takes in a dictionary dictionary whose keys 
and values are both integers. Using at least one loop, 
the function should find the sum of all keys in the dictionary 
and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function should 
return the string "keys".
If the sum of all values is greater than the sum of all keys, 
the function should return the string "values".
If keys and values have equal sums, the function should return the string "balanced".

def keys_v_values(dictionary):
    pass
Example Usage:

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

Example Output:
values
keys
"""


# def keys_v_values(dictionary):
#     key_total = 0
#     val_total = 0
    
    
#     for i in dictionary:
#         key_total += i
#         val_total += dictionary[i]
        
#     if key_total > val_total:
#         return "keys"
    
#     elif val_total > key_total:
#         return "values"
    
#     else:
#         return "balanced"
# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)

# dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# greater_sum = keys_v_values(dictionary2)
# print(greater_sum)

"""

Problem 5: Restock Inventory
Write a function restock_inventory() that updates an inventory
dictionary based on a restock list. It accepts two parameters:

current_inventory: a dictionary where each key-value pair represents an item
and its current stock in the inventory
restock_list: a dictionary where each key-value pair represents an item 
and the quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, 
it should be added. The function should return the updated dictionary current_inventory.

def restock_inventory(current_inventory, restock_list):
    pass
Example Input:

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

Example Output:
{
    "apples": 4 0,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}
"""

def restock_inventory(current_inventory, restock_list):
    
    for key in current_inventory: 
        if key in restock_list:
            current_inventory[key] += restock_list[key]
    for key in restock_list:
        if key not in current_inventory:
            current_inventory[key] = restock_list[key]
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))

"""
Problem 6: Calculate GPA
Write a function calculate_gpa() that calculates the grade point average (GPA)
for a student based on their course grades and returns the gpa as a float. 
The function takes in a dictionary report_card as a parameter where each 
key-value pair represents a course and the grade received in that course respectively. 
The grades are represented as strings ("A", "B", "C", "D", "F") 
and each grade corresponds to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

A GPA is calculated by finding the average of all grade points.

def calculate_gpa(report_card):
    pass
Example Usage:

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", 
"English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
Example Output: 3.3333333333333335
"""

# def calculate_gpa(report_card):
#     d = {"A" :4, "B": 3, "C" : 2, "D" : 1, "F" : 0}
    
#     total = 0
#     total_item = 0
    
#     for key,val in report_card.items():
       
#         if val in d:
#             total += d[val]
#             total_item += 1
    
#     return total / total_item 
# report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", 
# "English": "B", "Spanish": "A"}
# print(calculate_gpa(report_card))


"""
Problem 7: Best Book
Imagine you are working on a book review software like Goodreads. 
Write a function named highest_rated() that returns the book with the highest rating.

The function should take in a list of dictionaries named books as a parameter.
Each dictionary represents data associated with a book, including its title, author, 
and rating. The function should return the dictionary for the book with the highest 
rating.

def highest_rated(books):
    pass
Example Input:

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
Expected Output:

{"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
}
"""

# def highest_rated(books):
#     highest = books[0]
    
#     for book in books:
#         if book["rating"] > highest["rating"]:
#             highest = book
#     return highest


# books = [
#     {"title": "Tomorrow, and Tomorrow, and Tomorrow",
#      "author": "Gabrielle Zevin",
#      "rating": 4.18
#     },
#     {"title": "A Fortune For Your Disaster",
#      "author": "Hanif Abdurraqib",
#      "rating": 4.47
#     },
#     {"title": "The Seven Husbands of Evenlyn Hugo",
#      "author": "Taylor Jenkins Reid",
#      "rating": 4.40
#     }
# ]
# print(highest_rated(books))

"""
Problem 8: Index-Value Map
Write a function index_to_value_map() that takes in a list lst and returns 
a dictionary that maps the index of each element in lst to its value.

def index_to_value_map(lst):
    pass
Example Input: lst = ["apple", "banana", "cherry"]

Example Output: {0: "apple", 1: "banana", 2: "cherry"}
"""

# def index_to_value_map(lst):
#     mapping = {}
    
#     for i in range(len(lst)):
#         mapping[i] = lst[i]
#     return  mapping
# lst = ["apple", "banana", "cherry"]
# print(index_to_value_map(lst))         