def ex4(string):
    if len(string) > 10:
        string = string.upper()
    if len(string) <= 10:
        string = string.lower()
    return string