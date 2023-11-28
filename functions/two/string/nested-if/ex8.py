def ex8 (string1, string2):
    if len(string1) > len(string2):
        final = string1 + string2
    else:
        if len(string1) == len(string2):
            final = string1 + string2 + "!"
        else:
            final = string2 + string1
    return final