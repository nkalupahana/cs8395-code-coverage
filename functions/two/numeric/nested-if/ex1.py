def ex1(a, b):
  if a > b:
    result = a - b
    if result < 10:
      result = result + 5
  else:
    result = b - a
    if result > 10:
      result = result - 5
  return result