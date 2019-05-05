#Author     : Ishwar Jindal
#Created On : 24-Feb-2019 08:51 PM IST
#Purpose    : this file contain program to draw square

import turtle

#square using individual statements
def draw_square(t, length):
    t.fd(length)
    t.lt(90)
    
    t.fd(length)
    t.lt(90)
    
    t.fd(length)
    t.lt(90)

    t.fd(length)

#square using for loop
def draw_square_v1(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

t = turtle.Turtle()
draw_square_v1(t, 100)
