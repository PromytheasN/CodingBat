```Here I have 2 solutions for this problem, the first one is correct but it gives
time out error for some reason at codingbat that it should not. 
Second solution works there as well.
```

def make_chocolate(small, big, goal):
  
  #First of all we are checking if we have enough killos of chocolate
  #in total and if so if we have enough small bars of chocolate
  
  if small + big*5 < goal or big*5 - goal > small:
    return -1
  
  #Now we make sure that we use the maximum amount of big bars we can use.
  
  else:
    while goal >= 5 and big >= 1:
      goal -= 5
      big -= 1
  #while we used all our big bars the reminder is the amount of small bars
  #we need.
  
    return goal
    
    
    
   #Second solution.
   
   def make_chocolate(small, big, goal):
  
  #here we check if we have enough chocolate in total
   if small + big*5 < goal:
        return -1
  
  #Here we check the maximum amount of big bars we can use
    bigs_used = min(goal//5, big)
    
  #here we check how many small bars we need to use
    smalls_used = goal - 5*bigs_used
    
  #finally we check if we have enough small bars and return results!
  
    return smalls_used if smalls_used <= small else -1
