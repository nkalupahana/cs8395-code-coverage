def ex5(num1, num2):
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
    
    if result > 10:
        result = result * 0.5
    
    return result