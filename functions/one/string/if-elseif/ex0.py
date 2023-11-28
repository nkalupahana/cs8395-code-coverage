def ex0(string):
    if len(string) > 3:
        result = string[::-1]
    elif len(string) == 0:
        result = "Empty string"
    else:
        result = string.upper()

    return result