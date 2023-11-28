def ex5(x, y):
    if x > y:
        if x > 0:
            return x - y
        else:
            return x + y
    else:
        if y > 0:
            return x + y
        else:
            return x - y