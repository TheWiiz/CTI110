#CTI-110
#P4HW3_FACTORIAL
#Stephon Smith
#June 28, 2018
#

num = int(input("Please enter a number: ")) #get number
while num < 1:
    num = int(input("Please enter a positive number please: ")) #Make sure its not a negative

fct = 1

for ctn in range( 1, num+1):    #calculate
    fct = fct * ctn
print("\nThe factorial of", num, "is", fct) #print factorial
