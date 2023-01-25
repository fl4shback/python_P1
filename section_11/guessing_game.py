import random

state = None
random_number = random.randint(1,10)
print(f"Computer chose a number {random_number}")
pnumber = int(input("Please choose a number between 1 and 10 :"))

def verifnumber():
    if pnumber == random_number:
        print("You won")
        state = "won"
    elif pnumber > random_number:
        print("Your guess is too high")
        state = "toohigh"
    else:
        print("Your guess is too low")
        state = "toolow"
    return state

while state != "won":
    state = verifnumber()
    if state == "won":
        break
    pnumber = int(input("Choose a new number :"))
