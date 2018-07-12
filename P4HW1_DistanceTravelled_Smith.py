#CTI-110
#P4HW1_DISTANCE TRAVELLED
#Stephon Smith
#June 28, 2018
#


spd = float(input("What is the speed of your vehicle(MPH)? "))
tme = int(input("How long were you driving(Hours)? "))


print("Hour", "\tDistance Traveled")
print("-"*30)

for cth in range( 1, tme + 1):
    dst = spd * cth     #distance = speed * time
    print(cth, "\t", dst)












