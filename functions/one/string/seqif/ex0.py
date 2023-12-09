def ex0(str):
    if len(str) > 5:
        str = str.upper()
    if len(str) <= 5:
        str = str.lower()
    return str