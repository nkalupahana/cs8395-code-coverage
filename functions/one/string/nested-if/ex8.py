def ex8(string):
  if len(string) > 5:
    string = string.upper() 
    if string[0] == "A":
      string = string[1:]
  return string