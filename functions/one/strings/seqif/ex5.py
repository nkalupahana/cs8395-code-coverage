def ex5(string):
    if len(string) <= 6:
        string = string.upper()
    if len(string) > 6:
        string = string.lower()
    return string