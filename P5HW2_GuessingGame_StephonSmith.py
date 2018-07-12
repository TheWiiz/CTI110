#CTI-110
#Stephon Smith
#P5HW2 GuessingGame
#7/8/2018

def main():
    import random
    numg = 0

    num = random.randint(1,100)
    print("Guess a number between 1-100 you have 7 chances.")

    while numg < 5:
        print("take a guess: ")
        guess = input()
        guess = int(guess)

        numg = numg + 1
        if guess < num:
                print("Number to low")
        elif guess > num:
                print("Number to high")

    if guess == num:
        numg = str(numg)
        print("Well done You guessed the number in: ", numg)

    elif guess != num:
        number = str(num)
        print("Incorrect, the number was: ", num)

main()
restart = input("Would you like to continue? ")
while restart == "yes":
    main()
while restart == "no":
    exit()
