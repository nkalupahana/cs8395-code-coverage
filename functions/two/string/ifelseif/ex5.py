def ex5(str1, str2): 
    if len(str1) > len(str2):
        result = str1 + str2
    elif len(str1) < len(str2):
        result = str2 + str1
    else:
        result = str1[::-1] + str2
    return result