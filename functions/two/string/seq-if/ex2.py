def ex2(str1, str2):
    if str1.endswith(str2):
        return str1[:-len(str2)]
    else:
        if str2.endswith(str1):
            return str2[:-len(str1)]
    return str1 + str2