def ex3 (string): 
  if len(string) > 10: 
    string = string.upper() 
  elif len(string) < 5:
    string = string.lower() 
  else:
    string = string.title()
  return string