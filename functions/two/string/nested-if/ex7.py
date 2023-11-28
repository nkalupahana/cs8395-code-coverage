def ex7(string1, string2):
    if len(string1) > len(string2):
        long_string = string1
        short_string = string2
        result = long_string + short_string
    else:
        long_string = string2
        short_string = string1
        if len(short_string) > 5:
            result = long_string + short_string
        else:
            result = long_string * 2
    
    return result