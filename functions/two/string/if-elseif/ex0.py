def ex0(string1, string2):
    if len(string1) == len(string2):
        new_string = string1 + string2
    elif len(string1) > len(string2):
        new_string = string1[:len(string2)] + string2
    else:
        new_string = string2[:len(string1)] + string1
    return new_string