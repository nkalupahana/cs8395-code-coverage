def ex8(string):
    if 'a' in string:
        string = string.replace('a', 'b')
    elif 'b' in string:
        string = string.replace('b', 'c')
    else:
        string = string.replace('c', 'a')
    return string