def ex2(string):
    if len(string) > 5:
        result = string.upper()
    elif len(string) == 5:
        result = string.lower()
    else:
        result = string + '!'
    
    return result