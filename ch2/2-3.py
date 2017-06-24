"""
FizzBuzz!
"""

# Decide how far to iterate
steps = int(input("How far should I go?"))

# Begin loop
for i in range(1,steps+1):
  if i % 15 == 0:
    print("FizzBuzz!")
  elif i % 5 == 0:
    print("Buzz!")
  elif i % 3 == 0:
    print("Fizz!")
  else:
    print(i)
