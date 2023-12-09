def ex6(string):
    if len(string) > 5:
        if string[-1] == 's':
            string = string[::-1]
    else:
        string = string + 's'
        
    return string