def ex3(string1, string2):
    # manipulate strings
    if len(string1) > len(string2):
        result = string1 + string2
    else:
        result = string2 + string1
    # check result
    if "AB" in result:
        result = result.replace("AB", "")
    # return result
    return result