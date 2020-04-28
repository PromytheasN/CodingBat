#Here are 2 solutions of the round_sum problem
#One with a funtion within a function and one simpler one.

def round_sum(a, b, c):
    summ = 0
    for num in (a, b, c):
        roundedNum = round10(num)
        summ += roundedNum
    return int(summ)

#second function "helper" as requested at the excersize
def round10(num):
    if num%10 == 5:
        return round(num+1, -1)
    else:
        return round(num, -1)
        
#here is the simpler version (without 2 functions):

def round2(a, b, c):
    summ = 0
    for num in (a, b, c):
        if num%10 == 5:
            summ += round(num+1, -1)
        else:
            summ += round(num, -1)
    return summ
