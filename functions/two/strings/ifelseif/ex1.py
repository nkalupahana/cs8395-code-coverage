def ex1(string1, string2):
    if string1 == string2:
        return "The strings are the same."
    elif len(string1) > len(string2):
        return f"The first string is longer than the second by {len(string1) - len(string2)} characters."
    else:
        return f"The second string is longer than the first by {len(string2) - len(string1)} characters."