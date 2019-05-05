#Author         : Ishwar Jindal
#Created on     : 05-May-2019
#Modified on
#Purpose
#   This script contains program that determine if the the number a can be
#   expressed as some power of b.

def is_power(a,b):
    if a == b:
        return True
    elif a % b == 0 and is_power(a/b, b):
        return True
    else:
        return False

print ("main started")
number_to_check = 1
number_to_power_of = 2

if is_power(number_to_check, number_to_power_of):
    print (str(number_to_check) + " can be expressed as power of " + str(number_to_power_of))
else:
    print (str(number_to_check) + " cannot be expressed as power of " + str(number_to_power_of))

number_to_check = 1024
number_to_power_of = 2

if is_power(number_to_check, number_to_power_of):
    print (str(number_to_check) + " can be expressed as power of " + str(number_to_power_of))
else:
    print (str(number_to_check) + " cannot be expressed as power of " + str(number_to_power_of))

number_to_check = 15
number_to_power_of = 2

if is_power(number_to_check, number_to_power_of):
    print (str(number_to_check) + " can be expressed as power of " + str(number_to_power_of))
else:
    print (str(number_to_check) + " cannot be expressed as power of " + str(number_to_power_of))

number_to_check = 27
number_to_power_of = 3

if is_power(number_to_check, number_to_power_of):
    print (str(number_to_check) + " can be expressed as power of " + str(number_to_power_of))
else:
    print (str(number_to_check) + " cannot be expressed as power of " + str(number_to_power_of))

print ("main ended")


    
