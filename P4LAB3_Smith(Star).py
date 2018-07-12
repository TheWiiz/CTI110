#CTI 110
#P4LAB3_STAR
#Stephon Smith
#June 28, 2018
#

import turtle          
star = turtle

star.pencolor("yellow")
star.shape("turtle")

star.right(190)    

for i in (1,2,3,4,5):
    for i in (1,4,5):
        star.forward(50)
        star.right(120)
    star.forward(50)
    star.left(72)

 
