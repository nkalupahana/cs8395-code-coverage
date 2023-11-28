def ex7(num1, num2):
    if num1 < num2:
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by 0!"
    else:
        return num1 * num2