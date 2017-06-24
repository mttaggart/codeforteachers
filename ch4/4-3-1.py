def is_even(n):
  return n % 2 == 0
  
def even_filter(nums):
  res = []
  
  for n in nums:
    if is_even(n):
      res.append(n)
  
  return res
  
def odd_filter(nums):
  res = []
  for n in nums:
    if not is_even(n):
      res.append(n)
  
  return res
  
  
nums = list(range(1,101))
