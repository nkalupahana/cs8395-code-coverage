def ex0(string):
    if len(string) > 5:
        if '!' in string:
            string = string.replace('!', '?')
    return string