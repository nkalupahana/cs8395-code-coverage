def ex7(string1,string2):
    if len(string1) > len(string2):
        result = string1 + string2
    elif len(string1) < len(string2):
        result = string2 + string1
    else:
        result = string1 + string2
    return result