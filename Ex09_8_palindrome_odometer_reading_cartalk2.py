#Author : Ishwar Jindal
#Created On : 01-Jun-2019 02:21 PM IST
#Purpose : CarTalk 2


def is_palindrome(word):
    return word == word[::-1]

print("main started")

reading = 100000

while reading <= 999996:
    if is_palindrome(str(reading)[2:]) and is_palindrome(str(reading + 1)[1:]) and is_palindrome(str(reading + 2)[1:4]) and is_palindrome(str(reading + 3)):
        print(str.format("odometer reading of {} satisfies all four conditions", reading))
    reading = reading + 1
    
print("main ended")
