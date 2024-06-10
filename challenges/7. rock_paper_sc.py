'''
Make  simulation of the game. Use the images in the file to show the in the simulation.
utiliza Choise de ramdom
quiero que le pidas al usuario digite rock, paper or scissor y luego aleatoriamente la compu escoja uno y ver si gano y pierdo
'''
import random

# ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ["rock", "paper", "scissors"]
player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

if player_choice in options:
    computer_choice = random.choice(options)

    if player_choice == "rock":
        print("You chose:")
        print(rock)
    elif player_choice == "paper":
        print("You chose:")
        print(paper)
    else:
        print("You chose:")
        print(scissors)

    print("Computer chose:")
    if computer_choice == "rock":
        print(rock)
    elif computer_choice == "paper":
        print(paper)
    else:
        print(scissors)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")

