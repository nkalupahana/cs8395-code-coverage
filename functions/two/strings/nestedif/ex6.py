def ex6(string1, string2):
    if len(string1) > len(string2):
        result = string1[0:len(string2)] + string2
    else:
        if len(string1) < len(string2):
            result = string1 + string2[0:len(string1)]
        else:
            result = string1 + string2
    return result