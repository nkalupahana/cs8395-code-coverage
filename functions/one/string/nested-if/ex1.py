def ex1(string):

    if len(string) > 10:
        if string[-1] == 's':
            string = string[:-1]
    else:
        string = string + 's'
        
    return string