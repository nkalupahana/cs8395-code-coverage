def ex2(string1, string2):
    if string1 == string2:
        return string1
    elif string1 < string2:
        return string1 + string2
    else:
        return string2 + string1
    
print(ex2("Hello","World")) # Output: HelloWorld