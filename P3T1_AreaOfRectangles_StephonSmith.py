#CTI 110
#AREA OF RECTANGLE
#Stephon Smith
#June 15, 2018


#Get L/W rec1
l1 = int(input("What is the length of rectangle 1: "))
w1 = int(input("What is the length of rectangle 1: "))
#Get L/W rec2
l2 = int(input("What is the length of rectangle 2: "))
w2 = int(input("What is the length of rectangle 2: "))
#calculate area rec1
ar1 = l1 * w1
#print("Area of rectangle one: ", ar1)>>>               #Commented out because not needed for assignment but does work
#calculate area rec2
ar2 = l2 * w2
#print("Area of rectangle two: ", ar2)>>>               #Commented out because not needed for assignment but does work
#Determine which is greater
if ar1 > ar2:
    print("Rectangle 1 has the greater area.")
elif ar2 > ar1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both rectangles have the same area.")
