def ex9(string):
    if len(string) > 6:
        string = string[0:6] + "..."
    elif len(string) > 3 and len(string) <= 6:
        string = string[0:3] + "..."
    else:
        string = ""
    return string