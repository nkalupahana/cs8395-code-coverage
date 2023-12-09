def ex1(str1, str2):
  if len(str1) > len(str2):
    if len(str2) < 3:
      return str1
    else:
      return str1 + str2
  else:
    return str2 + str1