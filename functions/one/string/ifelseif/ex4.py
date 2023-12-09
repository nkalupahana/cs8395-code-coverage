def ex4(string):
    if len(string) == 0:
        return None
    elif len(string) == 1:
        return string.upper()
    else:
        return string[0].upper() + string[1:]

print(ex4("hello")) # Hello