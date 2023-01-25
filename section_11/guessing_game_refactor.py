from random import randint

replay = None

while replay != "n":
    cnumber = randint(1,10)
    pnumber = None

    while pnumber != cnumber:
        pnumber = int(input("Please choose a number [1-10] : "))
        if pnumber < cnumber:
            print("Your guess is too low")
        elif pnumber > cnumber:
            print("Your guess is too high")
        else:
            print("You won")

    replay = input("Do you want to play again ? (y/n) : ")

