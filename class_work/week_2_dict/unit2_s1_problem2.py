"""
Problem 1: Is Monotonic
Write a function is_monotonic() that takes in a list nums as a parameter 
and checks if it is either monotone increasing or monotone decreasing.
A list is monotone increasing if every element is either 
greater than or equal to the element before it.
A list is monotone decreasing if every element is 
either less than or equal to the element before it.
The function should return True if the given list is either
monotone increasing or decreasing and False otherwise.
Hint: This is a lists problem

def is_monotonic(nums):
    pass

Example Usage:
nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))

Example Output:
True
True
True
False
"""
# def is_monotonic(nums):
#     increasing = True
#     decreasing = True
#     for i in range(len(nums)- 1):
#         if nums[i] > nums[i + 1]:
#             increasing = False
#         if nums[i] < nums[i + 1]:
#             decreasing = False
#     return increasing or decreasing
# nums1 = [1,2,2,3,10]
# print(is_monotonic(nums1))
# nums2 = [12,9,8,3,1]
# print(is_monotonic(nums2))
# nums3 = [1,1,1]
# print(is_monotonic(nums3))
# nums4 = [1,9,8,3,5]
# print(is_monotonic(nums4))


"""
Problem 2: Student Directory
Write a function student_directory() that takes a list of student_names as a parameter
 and returns a dictionary of students, where each student in student_names is a key mapped to a unique numerical ;' ID.

def student_directory(student_names):
    pass
Example Input: student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
Example Output: {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}
"""

# def student_directory(student_names):
#     mapping_index = {}

#     for i in range(len(student_names)):
#         mapping_index[student_names[i]] = i + 1
#     return mapping_index
# student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
# print(student_directory(student_names))

"""
Problem 3: Dictionary Description
The following function get_description() takes in a dictionary info and a list keys as parameters. 
For each key in keys, the function prints the value associated with that key in info 
and prints None 
if the key does not exist in info.

However, the function has a bug! Copy the function into your IDE and run the code. 
Work with your group members to find the cause of the bug and correctly implement the function.

def get_description(info, keys):
    for key in keys:
	    print(info[key])
Example Input:

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
Expected Output:

Tom
engineer
None
"""
# def get_description(info, keys):
#     for key in keys:
#         if key in info:
#             print(info[key])
#         else:
#             print("None")

# info = {"name": "Tom", "age": "30", "occupation": "engineer"}
# keys = ["name", "occupation", "salary"]
# get_description(info, keys)

"""
Write a function sum_even_values() that returns the sum of all even values in a given dictionary. 
Assume the dictionary values are all integers.

def sum_even_values(dictionary):
    pass
Example Usage:

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
Example Output: 14
"""

# def sum_even_values(dictionary):
#     total = 0

#     for ch in dictionary:
#         if dictionary[ch] % 2 == 0:
#             total += dictionary[ch]
#     return total
# dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
# print(sum_even_values(dictionary))

"""
Write a function merge_catalogs() that combines two product catalogs, catalog1 and catalog2 as parameters. 
Each parameter is a dictionary where each key-value pair represents a product name and its price, respectively. 
If the same product exists in both catalogs, the price from the second catalog should overwrite the price in the first. 
Return the updated first catalog dictionary.

def merge_catalogs(catalog1, catalog2):
    pass
Example Input:

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
Example Output: {'apple': 1.0, 'banana': 0.75, 'cherry': 1.25}
"""
#def merge_catalogs(catalog1, catalog2):
    
    # for key,val in catalog2.items():
    #     catalog1[key] = catalog2[key]

        # if key in catalog1:
        #     catalog1[key] = catalog2[key]
        

#     return catalog1

# catalog1 = {"apple": 1.0, "banana": 0.5}
# catalog2 = {"banana": 0.75, "cherry": 1.25}
# print(merge_catalogs(catalog1, catalog2))

"""
Problem 6: Items to Restock
Write a function get_items_to_restock() that takes in a dictionary products that maps product names to their quantities 
and an integer restock_threshold as parameters. The function returns a list of products that have a 
value less than restock_threshold and need to be restocked. If products is empty, the function return an empty list.

def get_items_to_restock(products, restock_threshold):
    pass
Example Input:

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
Example Output: ['Product2', 'Product4']
"""
# def get_items_to_restock(products, restock_threshold):
#     new = []

#     for item in products:
#         if products[item] < restock_threshold:
#             new.append(item)
#     return new
# products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
# restock_threshold = 5
# print(get_items_to_restock(products, restock_threshold))

"""
Problem 7: Best Movie Genre
Imagine you're contributing to a move recommendation engine, 
and you're tasked with writing a function named most_popular_genre() that returns the genre with 
the highest average rating across all movies.

The function takes in a list of dictionaries named movies as a parameter. 
Each dictionary represents data associated with a movie, including its title, genre, and rating. 
The function calculates the average rating for each genre and returns the genre with
 the highest average rating.

def most_popular_genre(movies):
    pass
Example Usage:

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))
Example Output: Science Fiction
"""

# def most_popular_genre(movies):
#     highest = movies[0]
#     d = {}
#     highest_rating = float('-inf')
#     best_genre = None


#     for i in movies:
#         if i["genre"] in d:
#             d[i["genre"]].append(i["rating"])
#         else:
#             d[i["genre"]] = [i["rating"]]

#     for key in d:
#         avg = sum(d[key]) / len(d[key])
#         if avg > highest_rating:
#             highest_rating = avg
#             best_genre = key
#     return best_genre

        
# movies = [
#     {"title": "Inception",
#      "genre": "Science Fiction",
#      "rating": 8.8
#     },
#     {"title": "The Matrix", 
#      "genre": "Science Fiction",
#      "rating": 8.7
#     },
#     {"title": "Pride and Prejudice", 
#      "genre": "Romance",
#      "rating": 7.8
#     },
#     {"title": "Sense and Sensibility", 
#      "genre": "Romance",
#      "rating": 7.7
#     }
# ]

# print(most_popular_genre(movies))


"""
Problem 8: Quality Control
Write a function quality_control() that takes in a dictionary product_scores and 
an integer threshold as parameters. 
The dictionary product_scores has key-value pairs that represent 
a product ID and its quality rating.
If the product has a score greater than or equal to threshold, the function categorizes it as a "pass".
If the product has a score less than threshold, the function categorizes it as a "fail".
The function returns a new dictionary where the key-value pair is the product ID 
and whether it is a "pass" or "fail".

def quality_control(product_scores, threshold):
    pass
Example Input:

product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))
Example Output: {'x0123': 'pass', 'x0124': 'fail', 'x0125': 'pass', 'x0126': 'fail'}
"""

# def quality_control(product_scores, threshold):
#     for ch in product_scores:
#         if product_scores[ch] < threshold:
#             product_scores[ch] = 'fail'
#         else:
#             product_scores[ch] = 'pass'
#     return product_scores
# product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
# threshold = 60
# print(quality_control(product_scores, threshold))
