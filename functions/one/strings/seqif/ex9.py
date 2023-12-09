def ex9(string):
  if len(string) > 10:
    string = string[-10:]
  if len(string) == 10:
    string = string.upper()
  return string