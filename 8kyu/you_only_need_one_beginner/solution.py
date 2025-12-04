"""
Codewars Challenge:
You only need one - Beginner

Description:
You only need one - Beginner
You will be given an array a and a value x.
All you need to do is check whether the provided array contains the value.
a can contain numbers or strings. x can be either.
Return true if the array contains the value, false if not.
"""

def check(seq, elem):
    for s in seq:
        print(s, elem)
        if s == elem:
            return True
        else:
            continue
    return False


check([101, 45, 75, 105, 99, 107], 107)
