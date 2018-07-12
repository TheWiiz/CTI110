#CTI 110
#P4LAB1- SHAPES
#Stephon Smith
#JUNE 28, 2018
#

import turtle

x = turtle
for i in range(3):
    x.color("Cyan")
    x.forward(30)
    x.left(120)


x.penup()           #move turtle(x)
x.forward(30)
x.right(90)
x.pendown()         #New start position for x

for i in range(4):
    x.color("Purple")
    x.forward(30)
    x.right(90)
