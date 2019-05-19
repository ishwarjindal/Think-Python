# Author : Ishwar Jindal
# Created On : 19-ay-2019
# Purpose : Write Palindrome using inbuilt string functions

def is_palindrome(word):
    return word == word[::-1]

word = "pop"

if is_palindrome(word):
    print("[" + word + "] is palindrome")
else:
    print("[" + word + "] is not palindrome")
