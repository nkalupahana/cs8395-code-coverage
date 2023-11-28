def ex6(string1, string2):
    if len(string1) == len(string2):
        return string1 + string2
    elif len(string1) > len(string2):
        return string1[:len(string2)] + string2
    else:
        return string1 + string2[:len(string1)]