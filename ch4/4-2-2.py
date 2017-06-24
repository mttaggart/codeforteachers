def div(dividend, divisor):
  """
  Takes two ints and returns a tuple (quotient, remainder)
  """
  quotient = 0
  
  while dividend - divisor >= 0:
    dividend -= divisor
    quotient += 1
  
  return (quotient, dividend)