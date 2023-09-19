# Turtle is a Python module that provides a drawing board like feature, 
# which enables users to create pictures and shapes.


import turtle
 
# Set up the turtle screen and set the background color to black
screen = turtle.Screen()
screen.bgcolor("black")
 
# Create a new turtle and set its speed to the fastest possible
pen = turtle.Turtle()
pen.speed(0)
 
# Set the fill color to blue
pen.fillcolor("blue")
pen.begin_fill()
 
# Draw the circle with a radius of 100 pixels
pen.circle(100)
 
# End the fill and stop drawing
pen.end_fill()
pen.hideturtle()
 
# Keep the turtle window open until it is manually closed
turtle.done()
