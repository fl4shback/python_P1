from random import randint

### Init Global Variables
p1_score = 0
p2_score = 0
choices = ["rock", "paper", "scissors"]

### Define functions
def display_choices():
    print("Choose your weapon !")
    choice_id = 0
    while choice_id < len(choices):
        print(f"{choice_id}. {choices[choice_id].title()}")
        choice_id += 1

def print_winner(winner=None):
    if winner == "Player" or winner == "Computer":
        print(f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\n{winner} wins! \n Computer: {p2_score} \n Player: {p1_score}")
    else:
        print(f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nIt's a tie ! \n Computer: {p2_score} \n Player: {p1_score}")

def print_gwinner(gwinner):
    print(f"CONGRATS! {gwinner} won the game")

### Entering in a loop to restart the game until total score is 5
while p1_score + p2_score < 5:
    display_choices()

    ### Traps player in a loop until a valid choice is provided
    p1_choice = None
    looprun = 0
    valid_choice = range(0, 3)
    while p1_choice not in valid_choice:
        if looprun > 0:
            print(f"Please choose a valid number !")
            display_choices()
        p1_choice = input("Player, make your choice:")
        try:
            p1_choice = int(p1_choice)
        except:
            pass
        looprun += 1
    p1_choice = choices[p1_choice]

    ### Computer makes a choice
    computer_rand = randint(0, 2)
    p2_choice = choices[computer_rand]

    ### Prints match winner and adds score to player
    if p1_choice == p2_choice:
        print_winner()
    elif p1_choice == choices[0] and p2_choice == choices[2]:
        p1_score += 1
        print_winner("Player")
    elif p1_choice == choices[1] and p2_choice == choices[0]:
        p1_score += 1
        print_winner("Player")
    elif p1_choice == choices[2] and p2_choice == choices[1]:
        p1_score += 1
        print_winner("Player")
    else:
        p2_score += 1
        print_winner("Computer")

    ### Is this the end of the game ?
    if p1_score + p2_score == 4 and 1 in {p1_score, p2_score}:
        if p1_score > p2_score:
            print_gwinner("Player")
        else:
            print_gwinner("Computer")
        exit(0)
    elif p1_score + p2_score == 5 and p1_score > p2_score:
        print_gwinner("Player")
    elif p1_score + p2_score == 5 and p1_score < p2_score:
        print_gwinner("Computer")
    else:
        print(f"Round is not finished, play again. Total score: {p1_score + p2_score}/5")
