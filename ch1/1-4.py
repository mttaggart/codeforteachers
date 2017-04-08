"""
Number guesser!

Guess the number described by the expressed
assigned to the variable NUMBER
"""

NUMBER = 7 * 2 - 8 + 5

guess = int(input("What's your guess?"))

if guess == NUMBER:
  print("You got it!")
elif guess > NUMBER:
  print("Sorry, that's too high!")
else:
  print("Sorry, that's too low!")
