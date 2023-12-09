def ex4(str1, str2):
  if len(str1) > len(str2):
    result = str1 + str2
  if len(str2) > len(str1):
    result = str2 + str1
  return result