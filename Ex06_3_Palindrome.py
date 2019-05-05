#Author         : Ishwar Jindal 
#Created        : 05-May-2019
#Last Modified  : 05-May-2019
#Purpose
#   This script contains program that determine if the input
#   word is palindrome or not

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) == last(word) and is_palindrome(middle(word)):
        return True
    else:
        return False

print ("main started")

word = "ITI"
if is_palindrome(word):
    print (word + " is palindrome")
else:
    print (word + " is not palindrome")

print ("main ended")
