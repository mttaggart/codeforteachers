"""
Divider

Takes two terms and prints the integer quotient
"""

# We need our dividend and divisor

x = 15 # Dividend
y = 3 # Divisor

# And our quotient

quotient = 0

# Now our loop
while x - y >= 0:
    x -= y
    quotient += 1

# Print the quotient
print("This quotient is " + str(quotient))
