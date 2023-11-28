def ex4(x):
    if x < 0:
        # If the argument is less than 0, subtract it from 0
        x = 0 - x
    else:
        # If the argument is greater than or equal to 0, add 2
        x += 2
    return x