def ex9(x, y):
    if x > y:
        result = x - y
    else:
        result = y - x
    if result > 10:
        result += 10
    return result