# rock paper, scissors game

import random

playing = True
while playing:
    options = ("rock", "paper", "scissors")
    player = None
    computer = random.choice(options)

    player = input(
        "Enter a choice (rock, paper, scissors): ").lower()

    # if player == "q":
    #     print("Thanks")
    #     break

    if player not in options:
        continue

    elif player == computer:
        print("It's a tie!♎")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    print(f"Player: {player} \ncomputer: {computer}")

    if not input("Play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing")
