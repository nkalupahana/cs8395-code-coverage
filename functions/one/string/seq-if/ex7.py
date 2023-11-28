def ex7(string): 
    if len(string) > 5: 
        string = string.upper()
    if string.startswith("A"):
        string = "A" + string[1:]
    return string