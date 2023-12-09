def ex6(string):
    # Manipulates the string argument
    if string.isupper():
        string = string.lower()
    if string.startswith('a'):
        string = string.replace('a', 'the')
    return string