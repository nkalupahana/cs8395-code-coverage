def ex1(string1, string2):
    if len(string1) > len(string2):
        result = string1 + string2
    if len(string1) <= len(string2):
        result = string2 + string1
    return result