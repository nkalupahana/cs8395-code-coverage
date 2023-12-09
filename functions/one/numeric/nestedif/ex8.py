def ex8(x):
    if x == 0:
        return 0
    elif x > 0:
        x += 3
        if x > 10:
            x -= 5
    elif x < 0:
        x -= 5
        if x < -10:
            x += 3
    return x