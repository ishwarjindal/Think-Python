#Author     : Ishwar Jindal
#Created On : 09-Mar-2019 03:28 PM IST
#Purpose    : this file contain program to draw a Arc 


import turtle
import math

#polygon using for loop
def draw_ploygon(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

#draw arc 
def draw_arc(t, r, angle):
    
    circumfrence = 2 * (math.pi) * r * (angle/360)

    #for a circle the number of side of polygon should be a large number
    number_of_sides = 50

    #FORMULA
    #length * number of sides(n) = circumfrence
    
    length_of_each_side = circumfrence/number_of_sides

    draw_ploygon(t, length_of_each_side, number_of_sides, angle)


t = turtle.Turtle()
draw_arc(t, 100, 270)
