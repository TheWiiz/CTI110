#CTI-110
#P5HW1 - Test Average and Grade
#Stephon Smith
#July 3, 2018
#


def main():
    #initialize accumalator
    #get num of grades to total

    num = ginput()
    ave = calc_average(num)
    determine_grade(ave)

def calc_average (num):
    ttl = 0
    #run for loop to get the total
    for x in range(1, num + 1):
        grade = float(input("Enter grade: "))
        #total += grade
        ttl = ttl + grade
    ave = ttl / num
    return ave
def determine_grade (ave):
    if ave > 89 and ave < 101:
        print("You made an A!")
        print("Your grade of",ave,"is an A!")
    elif ave > 79 and ave < 90:
        print("You made an B!")
        print("Your grade of",ave,"is an B!")
    elif ave > 69 and ave < 80:
        print("You made an C!")
        print("Your grade of",ave,"is an C!")
    elif ave > 59 and ave < 70:
        print("You made an D!")
        print("Your grade of",ave,"is an D!")
    elif ave >= 0 and ave < 60:
        print("You made an F!")
        print("Your grade of",ave,"is an F!")
    else:
        print("Invalid input. Try again")
    #get the input
def ginput():
    num = int(input("How many grades would u like to enter? "))
    return num
main()
