def ex8(string1, string2):
  new_string = ""
  if len(string1) > len(string2):
    new_string = string1 + string2
  else:
    new_string = string2 + string1
  return new_string