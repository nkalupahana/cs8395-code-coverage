def ex4(string):
    # Manipulate the string
    if ' ' in string:
        string = string.replace(' ', '-')
    # Return the result
    return string