def ex7(string1, string2):
    if len(string1) > len(string2):
        result = string1 + string2
    else:
        result = string2 + string1
    if 'a' in result:
        result = result.replace('a', 'b')
    return result