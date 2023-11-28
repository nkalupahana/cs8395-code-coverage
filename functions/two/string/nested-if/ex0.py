def ex0(string1, string2):
    if len(string1) > len(string2):
        if string2 == 'up':
            return string1.upper()
        else:
            return string1.lower()
    else:
        if string1 == 'up':
            return string2.upper()
        else:
            return string2.lower()