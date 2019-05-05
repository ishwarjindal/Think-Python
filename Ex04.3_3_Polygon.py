#Author     : Ishwar Jindal
#Created On : 24-Feb-2019 08:54 PM IST
#Purpose    : this file contain program to draw polygon

import turtle
import math

#polygon using for loop
def draw_ploygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(int(360/n))

t = turtle.Turtle()
draw_ploygon(t, 100, 8)

