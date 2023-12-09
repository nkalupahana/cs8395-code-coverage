def ex3(string1, string2):
  if len(string1) >= len(string2):
    result = string1 + string2
  else:
    if string1 == string2:
      result = string1 + string2
    else:
      result = string2 + string1
  return result