#that's one way to solve this:
def close_far(a, b, c):
  if abs(a-b) <= 1 and abs(b-c) >= 2 and abs(a-c) >= 2:
    return True
  elif abs(a-c) <=1 and abs(a-b)>=2 and abs (b-c) >= 2:
    return True
  return False

#This is a quicker/simpler version of the solution:

def close_far(a, b, c):
  case1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
  case2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
  return case1 or case2
