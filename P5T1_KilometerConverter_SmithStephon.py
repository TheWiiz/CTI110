#CTI-110
#P5T1 - Kilometer converter
#Stephon Smith
#July 3, 2018
#


conversion_factor = 0.6214

def main ():
    #get the distance in Kilometers.
    kilometers = float(input("Enter a distance in Kilometers: "))

    #Display the distance converted to Miles.
    show_miles (kilometers)

    #convert km to mi/display results
    
def show_miles(km):
    #Calculate miles.
    miles = km * conversion_factor
    #Display the miles.
    print(km, " Kilometers equals ", miles, "Miles.")
main()
