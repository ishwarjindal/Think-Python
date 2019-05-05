import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, sides, length, angle):
    for i in range(sides):
        t.fd(length)
        t.lt(angle/sides)

def circle(t, radius):
    length = 10
    n = int((2*3.14*radius)/length)
    polygon(t, n, length, 360)

def arc(t, radius, angle):
    length = 10
    n = int((2*3.14*radius)/length)
    polygon(t, n, length, angle)
    

bob = turtle.Turtle()
#square(bob, 200)
#polygon(bob, 9, 100)
#circle(bob, 100)
arc(bob, 150, 180+90)

turtle.mainloop()
