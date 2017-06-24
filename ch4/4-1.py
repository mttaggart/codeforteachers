def double(n):
  """
  Takes a number n and doubles it
  """
  return n * 2
  

def double_nums(nums):
  doubled = []
  for num in nums:
    doubled.append(double(num))
    
  return doubled



nums_a = list(range(1,11)) # Is there a better way to say this?
nums_b = list(range(20,31))


# Print result
print(double_nums(nums_a))
print(double_nums(nums_b))