"""
Turtle is a Python feature that provides a drawing board, allowing us to control a turtle and draw on it. 
We can use functions such as 
turtle.forward() and turtle.right() to move the turtle around. 
Some commonly used turtle methods include:

Method	        Parameter	    Description
Turtle()	    None	        Creates and returns a new turtle object
forward()	    amount	        Moves the turtle forward by the specified amount
backward()	    amount	        Moves the turtle backward by the specified amount
right()	        angle	        Turns the turtle clockwise
left()	        angle	        Turns the turtle counterclockwise
penup()	        None	        Picks up the turtles Pen
pendown()	    None	        Puts down the turtles Pen
up()	        None	        Picks up the turtles Pen
down()	        None	        Puts down the turtles Pen
color()	        Color name	    Changes the color of the turtles pen
fillcolor()	    Color name	    Changes the color of the turtle will use to fill a polygon
heading()	    None	        Returns the current heading
position()	    None	        Returns the current position
goto()	        x, y	        Move the turtle to position x,y
begin_fill()	None	        Remember the starting point for a filled polygon
end_fill()	    None	        Close the polygon and fill with the current fill color
dot()	        None	        Leave the dot at the current position
stamp()	        None	        Leaves an impression of a turtle shape at the current location
shape()	        shapename	    Should be 'arrow', 'classic', 'turtle' or 'circle'


"""
# Creates and returns a new turtle object
import turtle
my_turtle = turtle.Turtle()

# Moves the turtle forward by the specified amount
my_turtle.forward(100)
for i in range(4):
    my_turtle.forward(50)
    my_turtle.right(90)         # Turns the turtle clockwise

# Turns the turtle counterclockwise
my_turtle.left(90)              # Turns the turtle counterclockwise
my_turtle.forward(100)
turtle.exitonclick()            # exit from the screen if and only if mouse is clicked
