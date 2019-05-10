#Author : Ishwar Jindal
#Created On : 05-May-2019
#Purpose : This file contains a script that determines greatest common divisior
#          between two numbers

def gcd(a,b):
    if a % b == 0:
        return b
    if a % b == 1:
        return 1;
    return gcd(a, a % b)

print ("main started")
a = 100
b = 20
print ("GCD of " + str(a) + "," + str(b) + " is " + str(gcd(a,b)))

a = 100
b = 16
print ("GCD of " + str(a) + "," + str(b) + " is " + str(gcd(a,b)))

a = 133
b = 39
print ("GCD of " + str(a) + "," + str(b) + " is " + str(gcd(a,b)))

a = 725
b = 125
print ("GCD of " + str(a) + "," + str(b) + " is " + str(gcd(a,b)))

a = 578
b = 72
print ("GCD of " + str(a) + "," + str(b) + " is " + str(gcd(a,b)))
print ("main ended")
