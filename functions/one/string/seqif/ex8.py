def ex8(string):
    if len(string) > 10:
        string = string + " is long!"
    if len(string) <= 10:
        string = string + " is short!"
    return string