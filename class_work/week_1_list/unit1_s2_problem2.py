"""
Problem 1: Convert Temperature
Write a function convertTemp() that takes in celsius as a parameter, 
which denotes the temperature in celsius. The variable is a non-negative 
floating point number rounded to two decimal places. In the function, 

Note that:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00

def convertTemp(celsius):
    pass
Example Usage:

temperatures = convertTemp(23.00)
print(temperatures)

Example Output:
[296.15, 73.40]
"""
def convertTemp(celsius):
    return [celsius + 273.15, celsius * 1.80 + 32.00]
temperatures = convertTemp(23.00)
print(temperatures)

"""
Problem 2: Average Score
Write a function average() that takes in a list of integers scores as a parameter and returns the average score.

def average(scores):
    pass
Example Usage:

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)
Example Output: 86.4
"""

# def average(scores):
#     total = 0
#     total_idx = 0
    
#     for i in range(len(scores)):
#         total += scores[i]
#         total_idx += 1
#     print(total)
#     print(total_idx)
#     return total / total_idx
# scores = [84,73,92,95,88]
# avg_score = average(scores)
# print(avg_score)


"""
Problem 3: Increment by 1
Write a function increment_values() that takes in a list of integers lst as a parameter and returns a new list containing each element incremented by 1.

def increment_values(lst):
    pass
Example Usage:

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)
Example Output:

[4, 6, 9, 3]
"""
# def increment_values(lst):
#     new = [x + 1 for x in lst]
#     return new

# lst = [3,5,8,2]
# new_lst = increment_values(lst)
# print(new_lst)

"""
Problem 4: Check for Number
Write a function check_num() that takes in a list of integers lst 
and an integer num as parameters and returns True if num is a 
value in lst and False otherwise.

def check_num(lst, num):
    pass
Example Usage:

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)
Example Output:

True
False
"""

# def check_num(lst, num):
#     if num in lst:
#         return True
#     else:
#         return False
# lst = [5,2,3,9,10]
# flag1 = check_num(lst,9)
# flag2 = check_num(lst,4)
# print(flag1)
# print(flag2)

"""
Problem 5: Missing Number
Write a function find_missing() that takes in a list nums containing n unique numbers in the range [0,n]. The function returns the only number in the range that is missing from the list.

def find_missing(nums):
    pass
Example Usage:

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)
Example Output: 3
"""
# def find_missing(nums):
#     total_range = 0
#     total = 0 
    
#     for n in nums:
#         total += n
#     for i in range(len(nums) + 1):
#         total_range += i
    
#     return total_range - total   
# nums = [2,4,1,0,5]
# missing_num = find_missing(nums)
# print(missing_num)

"""

Problem 6: Reverse List
Write a function reverse_list() that takes in a list lst as a parameter 
and returns a new list containing the elements of lst in reverse order.

def reverse_list(lst):
    pass
Example Usage:

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)
Example Output:

[5,4,3,2,1]
"""
# def reverse_list(lst):
#     return lst[::-1]
# lst = [1,2,3,4,5]
# rev_lst = reverse_list(lst)
# print(rev_lst)

"""
Problem 7: Get Odd Numbers
Write a function get_odds() that takes in a list of integers nums
and returns a list of all odd numbers in nums.

def get_odds(nums):
    pass
Example Usage:

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)
Example Output:

[5, 1, 5]
"""

# def get_odds(nums):
#     new = [x for x in nums if x % 2 == 1]
#     return new

# nums = [2,5,1,8,6,5]
# odd_nums = get_odds(nums)
# print(odd_nums)


"""
Problem 8: Multiplication Table
Write a function multiplication_table() that takes in an integer num 
and prints the multiples of that integer from 1 to 10.

def multiplication_table(num):
    pass
Example Usage: multiplication_table(7)

Example Output:

7
14
21
28
35
42
49
56
63
70
"""
# def multiplication_table(num):
#     for i in range(1, num + 1):
#         i =  i * num
        
#         print(i)
# multiplication_table(7)

"""
Problem 9: Create Number
Write a function list_to_number() that takes in a list digits where each item is a digit between 0-9. The function returns the number they represent when combined.

def list_to_number(digits):
    pass
Example Usage:

digits = [1,0,3]
number = list_to_number(digits)
print(number)
Example Output: 103
"""
# def list_to_number(digits):
#     new = ""
#     for n in digits:
#         new += str(n)
#     return new
    

# digits = [1,0,3]
# number = list_to_number(digits)
# print(number)

"""
Problem 10: Move Zeroes
Write a function move_zeroes() that takes in an integer list nums 
and returns a new list with all the 0 values moved to the end of the list. 
The relative non-zero elements in the original list should be maintained.

def move_zeroes(nums):
    pass
Example Usage:

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)
Example Output:

[1,2,3,4,0,0,0]

"""

# def move_zeroes(nums):
#     left = 0
    
#     for right in range(len(nums)):
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#     return nums

# nums = [1,0,2,3,0,0,4]
# new_nums = move_zeroes(nums)
# print(new_nums)

"""
Problem 11: Odd Indices
Write a function print_odd_indices() that takes in a list nums 
as a parameter and prints out items at odd indices in the list.

def print_odd_indices(nums):
    pass
Example Usage:

nums = [3,4,8,1,5,2]
print_odd_indices(nums)
Example Output:

# 4
# 1
# 2
# """          
# def print_odd_indices(nums):
#     for i in range(len(nums)):
#         if i % 2 == 1:
#             print(nums[i])
# nums = [3,4,8,1,5,2]
# print_odd_indices(nums)

"""
Problem 12: List Occurrences
Write a function find_all_occurrences() that takes in a list lst
and a value target as parameters and returns a list of all indices
where target is found in lst.

def find_all_occurrences(lst, target):
    pass
Example Usage:

lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)
Example Output:

[1,4,7,8]
"""

# def find_all_occurrences(lst, target):
#     new = [i for i in range(len(lst)) if lst[i] == target]
#     return new          
# lst = [1,2,6,5,2,1,3,2,2]
# index_list = find_all_occurrences(lst, 2)
# print(index_list)