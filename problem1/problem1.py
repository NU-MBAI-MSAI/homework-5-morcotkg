def is_leap_year(integer_1):
    if integer_1 % 4 == 0:
        if integer_1 % 100 == 0:
            if integer_1 % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    #comment