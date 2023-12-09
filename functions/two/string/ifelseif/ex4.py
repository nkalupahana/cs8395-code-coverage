def ex4(string1, string2):
    if len(string1) > len(string2):
        return string1 + string2
    elif len(string2) > len(string1):
        return string2 + string1
    else:
        return string1 + " " + string2