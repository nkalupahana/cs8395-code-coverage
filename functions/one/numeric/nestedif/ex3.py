def ex3(num):
    result = num
    if num > 0:
        result = num * 2
        if result > 10:
            result = result - 5
    return result