# This file contain code that draw flower on screen

import turtle
import math

def draw_arc(t, radius, angle, multiplier):
    """
    draw_arc draws an arc with specified radius and angle
    """
    print("draw_arc called with" + " radius=" + str(radius) + " angle=" + str(angle) + " multiplier=" + str(multiplier) + " turning angle" + str(multiplier*angle))
    # n * length = 2 * pi * radius (i.e. 360 degrees)
    # n * arc_length = 2 * pi * radius * angle/360
    # where n is number of steps in each movement
    arc_length = 2 * math.pi * radius * angle/360
    number_of_steps = int (arc_length/3) + 1 # +1 ensures that number of steps is atleast 1
    step_length = arc_length/number_of_steps
    step_angle = angle/number_of_steps
    
    for counter in range(number_of_steps):
        t.fd(step_length)
        t.lt(step_angle)

    t.lt(90 + multiplier*angle)
    
    for counter in range(number_of_steps):
        t.fd(step_length)
        t.lt(step_angle)
        
print ("Main started")
t = turtle.Turtle()

number_of_petals = 2
angle = 360/number_of_petals
multiplier = (number_of_petals/4)-1
radius = 100

## for drawing non overlapping flower
##for counter in range(number_of_petals):
##    draw_arc(t, radius, angle, multiplier)
##    t.lt(180)

## For drawing overlapping flower
for counter in range(number_of_petals*2):
    draw_arc(t, radius, angle, multiplier)
    t.lt(180/2 - multiplier*angle)



##radius = radius/2
##
##for counter in range(number_of_petals):
##    draw_arc(t, radius, angle, multiplier)
##    t.lt(180)

##t.lt(90)
##
##for counter in range(number_of_petals):
##    draw_arc(t, radius/2, angle, multiplier)
##    t.lt(180)
    
turtle.mainloop()
print ("Main ended")
