#David Meah - CS362 - HW7 - Q2

def isDivisibleBy4(x):
    if(x % 4) == 0:
        return True
    else:
        return False
   
def isNotDivisibleBy100(x):
    if(x % 100) == 0:
        return False
    else:
        return True

def isDivisibleBy400(x):
    if(x % 400) == 0:
        return True
    else:
        return False

def leapYearChecker(x):
    if(x % 4) == 0:
        if(x % 100) == 0:
            if(x % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
