# Two numbers are positive

def two_positive_numbers(a,b,c):
    if a < 0 and b > 0 and c > 0:
        print(True)
        return True
    elif a > 0 and b > 0 and c < 0:
        print(True)
        return True
    elif a > 0 and b < 0 and c > 0:
        print(True)
        return True
    elif a < 0 and b > 0 and c > 0:
        print(True)
        return True
    else:
        print(False)
        return False
    
two_positive_numbers(-4, 6, 0)     