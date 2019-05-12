#Author : Ishwar Jindal
#Created On : 11-May-2019
#Purpsoe : This file contains a script that calculate square root using Newton's method
import sys
import math

def right_justify(val, space):
    if len(str(val)) <= space:
        return str(val) + ' '*(space - len(str(val)))
    return str(val)[:space]

def mysqrt(a, x):
    while True:
        y = (x + a/x)/2
        if abs(y - x) < sys.float_info.epsilon:
            break
        x = y
    return y

def test_square_root():
    max_count = 20
    number = 1
    print(right_justify("a", 3) + " " + right_justify("mysqrt(a)", 13) + " " + right_justify("math.sqrt(a)", 13) + " " + "diff")
    print(right_justify("-", 3) + " " + right_justify("---------", 13) + " " + right_justify("------------", 13) + " " + "----")
    while True:
        if number > max_count:
            break
        my_sqrt = mysqrt(number, 20)
        math_sqrt = math.sqrt(number)
        delta = abs(my_sqrt - math_sqrt)
        print(right_justify(number, 3) + " " + right_justify(my_sqrt, 13) + " " + right_justify(math_sqrt, 13) + " " + str(delta))
        number = number + 1

print("main start")
test_square_root()
#a = 81
#x = 10
#print("my square root of " + str(a) + " is " + str(mysqrt(a, x)))
#print("square root of " + str(a) + " is " + str(math.sqrt(a)))
#print(str("[") + right_justify(1234567890111213,10) + str("]"))
print("main end")
    
