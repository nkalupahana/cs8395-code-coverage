def ex0(string1, string2):
    if len(string1) > len(string2):
        result = string1 + string2
    else:
        result = string2 + string1
    if result.isalpha():
        result = result.upper()
    else:
        result = 'Error'
    return result