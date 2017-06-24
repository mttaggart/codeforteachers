"""
RPS

Simple Rock, Paper, Scissors Game
"""
import random

# Beats
beats = {
  "rock" : "scissors",
  "paper" : "rock",
  "scissors" : "paper"
}

# Choices
choices = ["rock","paper","scissors"]

# Get player choice
player_choice = input("Choose rock, paper, or scissors")

if player_choice in choices:

  # Get computer choice
  computer_choice = random.choice(choices)
  print("Computer chose " + computer_choice)

  # Determine winner
  if player_choice == computer_choice:
    print("It's a tie!")
  elif beats[player_choice] == computer_choice:
    print("You win!")
  else:
    print("You lose!")
  
else:
  print("Not a valid choice!")
