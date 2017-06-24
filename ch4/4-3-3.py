def mult(x,y):
  product = 0
  for i in range(x):
    product += y
  return product

def div(dividend, divisor):
  quotient = 0
  while dividend - divisor >= 0:
    dividend -= divisor
    quotient += 1
  
  return (quotient, dividend)

def is_even(n):
  return n % 2 == 0
  
def even_odd_filter(nums, filter_evens=True):
  """
  Filters a list of ints for even/odd numbers
  Defaults to filtering for evens
  """
  res = []
  for n in nums:
    if is_even(n) == filter_evens:
      res.append(n)
  return res


def apply_fn(fn, nums, y):
  """
  Applies a given function fn to a list of ints 
  with the extra argument y
  """
  res = []
  for n in nums:
    res.append(fn(n,y))
  return res
  

nums = list(range(1,21))