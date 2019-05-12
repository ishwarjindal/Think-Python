#Author : Ishwar Jindal
#Created On : 11-May-2019
#Purpsoe : This file contains a script that calculate square root using Newton's method

def square_root(a, x):
    y = (x + a/x)/2
    return y


print("main start")
a = 4
x = 10
print("square root of " + str(a) + " is " + str(square_root(a, x)))
print("main end")
    
