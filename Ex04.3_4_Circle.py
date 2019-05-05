#Author     : Ishwar Jindal
#Created On : 09-Mar-2019 03:19 PM IST
#Purpose    : this file contain program to draw a circle using Polygon


import turtle
import math

#polygon using for loop
def draw_ploygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#draw circle using polygon
def draw_circle(t, r):
    
    circumfrence = 2 * (math.pi) * r

    #for a circle the number of side of polygon should be a large number
    number_of_sides = 40

    #FORMULA
    #length * number of sides(n) = circumfrence
    
    length_of_each_side = circumfrence/number_of_sides

    draw_ploygon(t, length_of_each_side, number_of_sides)


t = turtle.Turtle()
draw_circle(t, 50)
