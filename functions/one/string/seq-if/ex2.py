def ex2(string):
  if len(string) >= 3:
    string = string.upper()
  if len(string) < 3:
    string = string.lower()
  return string