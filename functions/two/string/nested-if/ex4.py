def ex4(string1, string2):
    if len(string1) > len(string2):
        if string1[0:len(string2)] == string2:
            return string1[len(string2):]
    return string1 + string2
    
print(ex4('hello', 'he')) # output => llo