"""
A mountain list is defined as a list that has at least three elements, 
where there exists some i with 0 < i < len(lst)-1 such that 
lst[0] < lst[1] < ... lst[i-1] < lst[i] and lst[i] > lst[i+1] > ... > lst[len(lst)-1].

Given such a mountain list lst as a parameter, write a function 
that finds and returns the highest peak (the index i of the maximum element).

def peak_index_in_mountain_list(lst):
    pass
Example Usage:

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)
Example Output: 2
"""

# def peak_index_in_mountain_list(lst):
#     highest = lst[0]
    
#     for n in lst:
#         if n > highest:
#             highest = n
#     return lst.index(highest)
# mountain_lst = [0,3,8,0]
# peak = peak_index_in_mountain_list(mountain_lst)
# print(peak)

"""
Problem 2: Build Inventory
Write a function build_inventory() that takes in a list of 
product_names and a corresponding list of product_prices as parameters. 
The function returns a dictionary representing the inventory of a small store. 
Each product name in product_names should be a key in the dictionary 
and the corresponding value should be the item price.

product_names[i] should be paired with product_prices[i] in the dictionary
where 0 <= i <= len(product_names). You may assume that 
product_names and product_prices are the same length.

def build_inventory(product_names, product_prices):
    pass
Example Input:

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))
Example Output:

{'Apple': 0.99, 'Banana': 0.5, 'Orange': 0.75}
"""

# def build_inventory(product_names, product_prices):
#     mapping = {}
    
#     for i in range(len(product_names)):
#         mapping[product_names[i]] = product_prices[i]
#     return mapping
# product_names = ["Apple", "Banana", "Orange"]
# product_prices = [0.99, 0.50, 0.75]
# print(build_inventory(product_names, product_prices))

"""
Problem 3: Update or Warn
Write a function update_or_warn() that takes in a dictionary records, 
a key item, and a new value update_value as parameters. 
The function updates the value of item in records with update_value if item exists. 
If item does not exist, it should print "<item> not found!" 
and not modify the dictionary.

def update_or_warn(records, item, update_value):
    pass
Example Usage:

records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "grape", 4)
# Print the input dictionary after running the function to check if it was modified
print(records) 
update_or_warn(records, "banana", 5)
print(records)
Example Output:

grape not found!
{'apple': 1, 'banana': 2, 'orange': 3}
{'apple': 1, 'banana': 5, 'orange': 3}
"""

# def update_or_warn(records, item, update_value):
#     if item in records:
#         records[item] = update_value
#     else:
#         print(f"{item} not found!")
#     return records

# records = {"apple": 1, "banana": 2, "orange": 3}
# update_or_warn(records, "grape", 4)
# # Print the input dictionary after running the function to check if it was modified
# print(records) 
# update_or_warn(records, "banana", 5)
# print(records)


"""
Problem 4: Attendance Rate
Write a function attendance_rate() that takes in a dictionary 
attendance_list as a parameter. The function maps student names to their 
attendance status ("Present" or "Absent"), and returns the percentage of students 
who are present.

def attendance_rate(attendance_list):
	pass
Example Usage:

attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))
Example Output: 50.0
"""

# def attendance_rate(attendance_list):
#     total_student = 0
#     total_present = 0

#     for ch in attendance_list:
#         total_student += 1
#         if attendance_list[ch] == "Present":
#             total_present += 1
#     return (total_present / total_student) * 100

# attendance_list = {
#     "Bluey": "Present", 
#     "Bingo": "Absent", 
#     "Snickers": "Present", 
#     "Winton": "Absent"
# }
# print(attendance_rate(attendance_list))



"""
Problem 5: Average Book Ratings
Write a function average_book_ratings(), that calculates the average rating for each 
book in a collection. 
The function takes one parameter: a dictionary book_ratings where each 
key-value pair represents a book title 
and a list of its ratings, respectively. Ratings are represented as floating-point numbers. 
The function should return a new dictionary with book titles as keys and their average rating.

def average_book_ratings(book_ratings):
    pass
Example Input:

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
Example Output:

{'The Great Gatsby': 4.166666666666667, 
'To Kill a Mockingbird': 4.675000000000001}
"""
# def average_book_ratings(book_ratings):
#     for key, val in book_ratings.items():
#         book_ratings[key] = sum(val) / len(val)
#     return book_ratings
# book_ratings = {
#     "The Great Gatsby": [4.5, 3.0, 5.0],
#     "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
# }
# print(average_book_ratings(book_ratings))

"""
Problem 6: Odd Keys Even Values
Write a function odd_keys_even_values() that takes in dictionary as a parameter, 
a dictionary with integer keys and values. The function returns a list of keys that are odd 
where their corresponding values are even.

def odd_keys_even_values(dictionary):
    pass
Example Usage:

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)
Example Output:

[1, 5]
"""
# def odd_keys_even_values(dictionary):
#     new = []

#     for key, val in dictionary.items():
#         if key % 2 == 1 and val % 2 == 0:
#             new.append(key)
#     return new
# dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
# final_list = odd_keys_even_values(dictionary)
# print(final_list)

"""
Problem 7: Best Team
You're developing an analytics tool for a sports league. Your task is to write a 
function named team_with_best_average_score() that returns the team with the 
highest average score over a season.
      
The function should accept a list of dictionaries named games as a parameter. 
Each dictionary represents data from a game, including the "team_name", 
and the "score" they achieved in that game. 
The function calculates the average score for each team across all games 
and returns the team with the highest average score.

def team_with_best_average_score(games):
    pass
Example Usage:

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]

print(team_with_best_average_score(games))
Example Output: Tigers
"""

# def team_with_best_average_score(games):
#     d = {}
#     highest_score = float('-inf')
#     best_team = None

#     for key in games:
#         if key["team_name"] not in d:
#             d[key["team_name"]] = [key["score"]]
#         else:
#             d[key["team_name"]].append(key["score"])

#     for key,val in d.items():
#         average = sum(val) / len(val)
#         if average > highest_score:
#             highest_score = average
#             best_team = key
#     return best_team


# games = [
#     {"team_name": "Lions",
#      "score": 23
#     },
#     {"team_name": "Tigers", 
#      "score": 30
#     },
#     {"team_name": "Lions", 
#      "score": 27
#     },
#     {"team_name": "Bears", 
#      "score": 20
#     },
#     {"team_name": "Tigers", 
#      "score": 24
#     },
#     {"team_name": "Bears", 
#      "score": 22
#     }
# ]
# print(team_with_best_average_score(games))



"""

Problem 8: First Unique Items

Write a function find_unique_items() that takes two lists list_a and list_b as parameters. 
The function identifies unique items from the lists and returns a dictionary with the items as keys 
and a boolean value as the value indicating whether the item is unique to the 
first list (True) or not (False).

def find_unique_items(list_a, list_b):
    pass
Example Input:

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
Example Output: {"carrot": True, "date": False}

"""

# def find_unique_items(list_a, list_b):

#     d = {}

#     for item in list_a:
#         if item not in list_b:
#             d[item] = True
    

#     for item in list_b:
#         if item not in list_a:
#             d[item] = False
#     return d
# list_a = ["apple", "banana", "carrot"]
# list_b = ["apple", "banana", "date"]

# print(find_unique_items(list_a, list_b))