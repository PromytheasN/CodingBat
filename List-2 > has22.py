#my First solution should work but it seems that CodingBat sometimes creates error that I don't get in Jupyter or VScode.

#1st solution

def has22(nums):
  for i in range(len(nums)-2):
    
    #or on Juypiter it even works like this: for i in num:
    
    return nums[i:i+2] == [2,2]
    
 #2nd solution accepted by codingbat
 
 def has22(nums):
  for i in range(len(nums)-1):
    if nums[i:i+2] == [2,2]:
      return True
  return False
    
