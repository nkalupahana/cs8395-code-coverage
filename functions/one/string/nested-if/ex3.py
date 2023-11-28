def ex3(string):
  if len(string) > 5:
    new_string = string.replace('a', 'e')
    if new_string[0] == 'e':
      return new_string.upper()
    else:
      return new_string
  else:
    return string