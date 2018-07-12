#CTI-110
#P4HW2_RUNNING TOTAL
#Stephon Smith
#June 28, 2018
#


num = float(input("Please enter first number or a negative " + \
                  "number to quit: "))
total = 0
while num > -1:
    total = total + num
    num = float(input("Enter the next number or " + \
                      "negative number to quit: "))

print("\nThe sum of all the numbers you entered is", total)
