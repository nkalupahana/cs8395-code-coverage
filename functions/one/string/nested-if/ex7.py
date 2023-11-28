def ex7(string):
  if len(string) > 0:
    if string[0] == 'a' or string[0] == 'e' or string[0] == 'i' or string[0] == 'o' or string[0] == 'u':
      string = string + 'way'
    else:
      string = string[1:] + string[0] + 'ay'
  return string