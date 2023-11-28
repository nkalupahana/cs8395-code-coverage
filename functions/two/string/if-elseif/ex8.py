def ex8(string1, string2):
    if len(string1) < len(string2):
        result = string2 + string1
    elif len(string1) > len(string2):
        result = string1 + string2
    else:
        result = string1 + " " + string2
    return result