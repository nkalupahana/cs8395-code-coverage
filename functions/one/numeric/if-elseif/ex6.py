def ex6(num):
    if num < 0:
        num = 0
    elif (num % 2 != 0):
        num = num + 1
    else:
        num = num * 2
    return num