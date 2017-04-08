"""
Even/Odd Checker

Takes input from user and determines
whether that number is even or odd.
"""

# Get input from user
test = int(input("What number should I test?"))
# print(test)
if test % 2 == 0:
  print("It's even!")
else:
  print("It's odd!")
