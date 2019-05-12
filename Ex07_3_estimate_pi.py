#Author : Ishwar Jindal
#Created On : 12-May-2019
#Purpose : This script calculates the value of pi using Ramanujuam's formula
import math

def estimate_pi():
    counter_k =0
    last_term = 0
    summition = 0
    
    while True:
        print(str(counter_k + 1))
        last_term = (math.factorial(4*counter_k) * (1103 + 26390 * counter_k)) / (math.pow(math.factorial(counter_k),4) * (math.pow(396 , 4*counter_k)))
        counter_k = counter_k + 1
        if last_term < 1e-15:
            break
        summition = summition + last_term
        
    inverse_pi = (2 * math.sqrt(2)/9801) * summition
    return 1/inverse_pi
    

print("main started")
estimated_pi = estimate_pi()
print("Estimated pi = " + str(estimated_pi) + " : math.pi = " + str(math.pi) + " : delta is " + str(abs(estimated_pi - math.pi)))
print("main ended")
