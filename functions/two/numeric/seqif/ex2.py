def ex2(num1, num2):
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
    
    if result > 5:
        result = result * 2
    else:
        result = result / 2
    
    return result