def ex9(string1, string2):
  result = ""
  if len(string1) > len(string2):
    result = string2 + string1
    if len(string1) > 5:
      result = string1[::-1] + string2
  return result