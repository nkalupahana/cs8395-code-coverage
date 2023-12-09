def ex2(string):
  if len(string) > 10:
    string = string.upper()
    if string[0] == "A":
      string = string.replace("A", "Z")
  return string