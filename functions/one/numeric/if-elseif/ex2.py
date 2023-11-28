def ex2(num):
    if num < 0:
        num = abs(num)
    elif num > 0 and num < 10:
        num = num * 10
    else:
        num = num / 2
    return num