def sum13(nums):
  return sum(current for (prev,current) in zip([None] + nums[:-1], nums) 
              if prev != 13 and current !=13)
