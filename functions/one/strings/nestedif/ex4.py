def ex4(string):
    if len(string) > 5:
        new_string = string[::-1]
        if " " in new_string:
            new_string = new_string.replace(" ", "+")
        return new_string
    else:
        return string