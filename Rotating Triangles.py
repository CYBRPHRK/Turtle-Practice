import turtle
import colorsys

# Creating an instance of class Turtle
t = turtle.Turtle()
# Creating a singleton object of a TurtleScreen subclass
s = turtle.Screen()

# Setting screen color to 'black'
s.bgcolor('black')

# Setting the speed of the turtle to 0 (fastest)
t.speed(0)

# Variables to create variation in color
n = 100
h = 0

for i in range(180):
    # Creating a color instance and the value of h is changed in every iteration
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n

    # Setting the pen color for the turtle and turn the turtle to the left
    t.color(c)
    t.left(i)

    # Code to create Triangles
    for j in range(3):
        t.forward(i*4)
        t.left(120)
