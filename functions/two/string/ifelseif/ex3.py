def ex3(string1, string2):
    if len(string1) > len(string2):
        return string1.upper() + string2.lower()
    elif len(string1) < len(string2):
        return string1.lower() + string2.upper()
    else:
        return string1 + string2