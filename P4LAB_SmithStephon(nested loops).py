#CTI 110
#P4LAB- NESTED LOOPS
#STEPHON SMITH
#JUNE 28, 2018
#
import turtle
import random
pete = turtle

# add some display options
pete.pensize(6)            # increase pensize
pete.shape("turtle")


 
pete.left(180)             #draw in different direction
color = ["Purple", "Blue", "Pink", "Cyan", "Yellow", "maroon"]
# draw a star
for i in (1,2,3,4,5):
    # turn other direction; triangles on outside
    for x in range(3):
        pete.color(random.choice(color))
        pete.forward(100)
        pete.right(120)
    pete.forward(100)
    pete.left(72)



