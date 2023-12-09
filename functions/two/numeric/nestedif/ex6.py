def ex6(x, y):
    if x > y:
        result = x - y
        if result % 2 == 0:
            result *= 2
    else:
        result = y - x
        if result % 2 == 0:
            result /= 2
    return result