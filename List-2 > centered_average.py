def centered_average(nums):
  nums.remove(max(nums)), nums.remove(min(nums))
  average = sum(nums)//len(nums)
  return average
