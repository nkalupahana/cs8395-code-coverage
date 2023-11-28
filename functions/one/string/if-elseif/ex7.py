def ex7(str):
  if len(str) > 5:
    return str.upper()
  elif len(str) < 3:
    return str.lower()
  else:
    return str[::-1]