def ex8(num):
    if num > 0:
        result = num + 5
    else:
        result = num - 5
    
    if result > 0:
        result = result * 2
    else:
        result = result / 2
    
    return result