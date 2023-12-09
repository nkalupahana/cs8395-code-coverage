def ex2(string1, string2):
    if len(string1) > len(string2):
        combo_string = string1 + string2
        if len(combo_string) > 10:
            return combo_string.upper()
        else:
            return combo_string.lower()
    else:
        return string1 + string2