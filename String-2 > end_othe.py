"""

Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.
"""


def end_other(a, b):
    a,b = a.lower(), b.lower()
    return (b.endswith(a) or a.endswith(b))
    
#or you can: return a == b[-(len(a)):] or b == a[-(len(b)):]
#or you can: return a in b[-(len(a)):] or b in a[-(len(b)):]
