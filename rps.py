from random import randint

### Init Global Variables
p1_score = 0
p2_score = 0
choices = ["rock", "paper", "scissors"]

### Entering in a loop to restart the game until total score is 5
while p1_score + p2_score < 5:

    ### Prints choices
    print("Choose your weapon !")
    choice_id = 0
    for choice in choices:
        print(f"{choice_id}. {choice.title()}")
        choice_id += 1

    ### Traps player in a loop until a valid choice is provided
    p1_choice = None
    reloop = 0
    while p1_choice != 0 and p1_choice != 1  and p1_choice != 2:
        if reloop == 1:
            print("Please choose a valid value !")
        p1_choice = input("Player 1, make your choice:")
        reloop = 1
        try:
            p1_choice = int(p1_choice)
        except:
            print("Please input a number !")
            reloop = 0
    p1_choice = choices[p1_choice]

    ### Computer makes a choice
    computer_rand = randint(0, 2)
    p2_choice = choices[computer_rand]

    ### Prints match winner and adds score to player
    ############################################################################################################################################
    ### tie = f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nIt's a tie ! \n Computer: {p2_score} \n Player: {p1_score}"       ###
    ### p1_wins = f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nPlayer 1 wins! \n Computer: {p2_score} \n Player: {p1_score}" ###
    ### p2_wins = f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nComputer wins! \n Computer: {p2_score} \n Player: {p1_score}" ###
    ###     Can't do it this way because f-strings are populated before the conditions apply so, the incremented score doesn't display       ###
    ############################################################################################################################################
    if p1_choice == p2_choice:
        print(f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nIt's a tie ! \n Computer: {p2_score} \n Player: {p1_score}")
    elif p1_choice == choices[0] and p2_choice == choices[2]:
        p1_score += 1
        print(f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nPlayer 1 wins! \n Computer: {p2_score} \n Player: {p1_score}")
    elif p1_choice == choices[1] and p2_choice == choices[0]:
        p1_score += 1
        print(f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nPlayer 1 wins! \n Computer: {p2_score} \n Player: {p1_score}")
    elif p1_choice == choices[2] and p2_choice == choices[1]:
        p1_score += 1
        print(f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nPlayer 1 wins! \n Computer: {p2_score} \n Player: {p1_score}")
    else:
        p2_score += 1
        print(f"Player: {p1_choice.title()} Computer: {p2_choice.title()}\nComputer wins! \n Computer: {p2_score} \n Player: {p1_score}")

    ### Is this the end of the game ?
    if p1_score + p2_score == 5 and p1_score > p2_score:
        print("CONGRATS, Player won the game")
    elif p1_score + p2_score == 5 and p1_score < p2_score:
        print("CONGRATS, Computer won the game")
    else:
        print(f"Round is not finished, play again. Total score: {p1_score + p2_score}/5")
