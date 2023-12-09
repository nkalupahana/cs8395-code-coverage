def ex5(string1, string2):
    if len(string1) > len(string2):
        new_string = string1 + string2
    else:
        new_string = string2 + string1
    if 'a' in new_string:
        final_string = new_string.upper()
    else:
        final_string = new_string.lower()
    return final_string