#Stephon Smith
#7/3/18


####First example- Blocky Snowflake(Shapes)
##import turtle
##import random
##
##elsa = turtle
##elsa.color("cyan")
##elsa.bgcolor("grey")
##
##colours = ["cyan", "purple", "white", "blue"]
##for i in range(10):            #turns shape to make figure
##    for i in range(2) :         #Makes parralelagram
##        elsa.color(random.choice(colours))
##        elsa.forward(100)
##        elsa.left(60)
##        elsa.forward(100)
##        elsa.left(120)
##    elsa.right(36)             #turns shape to make figure

###Second example- Skinny Snowflake(No Shapes)
##
import turtle
import random

elsa = turtle
elsa.bgcolor("grey")

colours = ["cyan", "purple", "white", "blue"]

elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

def branch():
    for i in range(3):
        colours.random
     for i in range(3):
         elsa.forward(30)
        elsa.backward(30)
        elsa.right(45)
     for i in range(1):
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)

    for i in range(8):
    branch()
    elsa.left(45)
    elsa.exitonclick()
