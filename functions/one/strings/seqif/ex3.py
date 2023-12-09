def ex3(string):
    if len(string) > 5:
        string = string.lower()
    if len(string) <= 5:
        string = string.upper()
    return string