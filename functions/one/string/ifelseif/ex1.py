def ex1(string):
  if len(string) == 0:
    return 'Empty string'
  elif len(string) == 1:
    return string.upper()
  else:
    return string[0:len(string)//2].lower() + string[len(string)//2:].upper()