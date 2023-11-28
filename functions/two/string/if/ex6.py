def ex6(arg1, arg2):
    result = ""
    if len(arg1) != len(arg2):
        result = arg1 + arg2
    else:
        result = arg2 + arg1
    return result