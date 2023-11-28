def ex4(num1, num2):
    if num1 > num2:
        result = num1 - num2
    else:
        result = num1 + num2
 
    if result > 0:
        result = result / 2
    else:
        result = result * 2
        
    return result