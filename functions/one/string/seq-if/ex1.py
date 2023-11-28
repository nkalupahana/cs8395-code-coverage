def ex1(string):
    if len(string) % 2 == 0:
        string = string.upper()
    if len(string) % 2 != 0:
        string = string.lower()
    return string