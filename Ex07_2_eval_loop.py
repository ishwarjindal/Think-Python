#Author : Ishwar Jindal
#Created On : 12-May-2019
#Purpose : This file contains a script that takes input from user as expression and evaluate it using math.eval. It stop asking when user enters "done"

import math

def eval_loop():
    while True:
        user_input = input("Enter expression > ")
        if user_input == "done":
            break
        print(eval(user_input))

print ("main started")
eval_loop()
print ("main ended")
