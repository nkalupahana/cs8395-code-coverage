def ex5(string1, string2):
    new_string = string1 + ' ' + string2
    if len(new_string) > 10:
        new_string = new_string.upper()
    return new_string