"""
Problem 1: Perfect Match
Copy and paste the following function:

def match_made(dictionary):
    for key, value in dictionary.items():
        print( f"{key} and {value} are a perfect match.")
Add code to your IDE so that your program prints out the following to the console:

Peanut butter and Jelly are a perfect match.
Spongebob and Patrick are a perfect match.
Ash and Pikachu are a perfect match.
"""

# def match_made(dictionary):
#     for key, value in dictionary.items():
#         print( f"{key} and {value} are a perfect match.")
# dictionary = {"Peanut butter":"Jelly", "Spongebob":"Patrick", "Ash":"Pikachu"}
# match_made(dictionary)

"""
Problem 2: Remove Char
Write a function remove_char() that takes in a string s and 
an integer n as parameters, The function returns a new string with the 
nth character removed where 0 < n < len(s).

def remove_char(s, n):
    pass
Example Usage:

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
Example Output: typo
"""
# def remove_char(s, n):
#     return s[:n] + s[n+1:]
# s = "typpo"
# fixed_s = remove_char(s, 2)
# print(fixed_s)

"""
Problem 3: Count Vowels
Write a function vowel_count() that takes in a string s 
as a parameter and returns the number of vowels in the given string.

def vowel_count(s):
    pass
Example Usage:

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)
Example Output:

3
10
0
"""

# def vowel_count(s):
#     vowels = "a,e,i,o,u"
#     count = 0

#     for char in s:
#         if char.lower() in vowels:
#             count += 1
#     return count
# my_str = "hello world"
# my_str2 = "aAaAaAaAAA"
# my_str3 = "ths strng s mssng vwls"

# count1 = vowel_count(my_str)
# print(count1)
# count2 = vowel_count(my_str2)
# print(count2)
# count3 = vowel_count(my_str3)
# print(count3)

"""
Problem 4: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence as a 
parameter and returns the string with the sentence but with the order of the words reversed. 
The sentence will only contain alphabetic characters and spaces to separate the words. 
If there is only one word in the sentence, the function returns the original string.

def reverse_sentence(sentence):
    pass
Example Input: sentence = "I solemnly swear I am up to no good"

Example Output: "good no to up am I swear solemnly I"

"""

# def reverse_sentence(sentence):
#     new = sentence.split()
#     return " ".join(new[::-1])
# sentence = "I solemnly swear I am up to no good"
# print(reverse_sentence(sentence))
# def reverse_sentence(sentence):
#     new = sentence.split()
#     res = ""
    
#     for i in range(len(new)-1,-1,-1):
#         res += new[i] + " "
#     return res.strip()
# sentence = "I solemnly swear I am up to no good"
# print(reverse_sentence(sentence))
    

"""
Problem 5: String Compression
Write a function that takes in a string my_str as a parameter 
and performs basic string compression using counts of repeated characters.

For example, the string "aabcccccaaa" would become "a2b1c5a3". 
If the compressed string does not become smaller than the original string, 
return the original string. Assume the string only has alphabetic characters.

def compress_string(my_str):
    pass
Example Usage:

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)
Example Output:

a5b2c3d1
abcde 
# did not convert my_str2 because `a1b1c1d1e1` is double the length

"""

# def compress_string(my_str):
#     count = 1
#     curr_str = my_str[0]
#     new = ""

#     for i in range(1, len(my_str)):
#         if my_str[i] == my_str[i - 1]:
#             count += 1
#         else:
#             new += curr_str + str(count)
#             curr_str = my_str[i]
#             count = 1
#     new += curr_str + str(count)
#     return new if len(new) < len(my_str) else my_str
# my_str = "aaaaabbcccd"
# compressed_Str = compress_string(my_str)
# print(compressed_Str)

# my_str2 = "abcde"
# compressed_Str2 = compress_string(my_str2)
# print(compressed_Str2)

"""
Problem 6: Needle in a Haystack
Write a function find_the_needle() that takes in two string parameters: 
a needle and a haystack. The function returns the index of the first occurrence of 
needle in haystack, or -1 if needle is not part of haystack.

def find_the_needle(haystack, needle):
    pass
Example Usage:

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))
Example Output:

2
-1

"""

# def find_the_needle(haystack, needle):
#     return haystack.find(needle)
# haystack = "tobeornottobe"
# needle = "be"
# print(find_the_needle(haystack, needle))

# haystack2 = "leetcode"
# needle2 = "leeto"
# print(find_the_needle(haystack2, needle2))

# def find_the_needle(haystack, needle):
#     for i in range(len(haystack) - len(needle) + 1):
#         if haystack[i: i + len(needle)] == needle:
#             return i
#     return -1
# haystack = "tobeornottobe"
# needle = "be"
# print(find_the_needle(haystack, needle))

# haystack2 = "leetcode"
# needle2 = "leeto"
# print(find_the_needle(haystack2, needle2))