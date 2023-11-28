def ex5(string):
    if len(string) >= 10:
        if string.isupper():
            return string.lower()
        else:
            return string.upper()
    else:
        return string