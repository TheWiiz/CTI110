#CTI 110
#P3LAB - DEBUGGING
#Smith
#June 22, 2018
#



def main():
# This program takes a number grade and outputs a letter grade.

# system uses 10-point grading scale

# TO DO: define the rest of the scores

    score = float(input('Enter grade: '))           #define variables
    Asc = 90
    Bsc = 80
    Csc = 70
    Fsc = 69

    if score >= 101:                                #Determine letter grade
            print('Your grade is A+')
    elif score >= Asc:
        print('Your grade is: A')
    elif score >= Bsc:
            print('Your grade is: B')
    elif score >= Csc:
            print('Your grade is: C')
    elif score <= Fsc:
            print('Your grade is: F')



# program start
main()
