def ex5(num1, num2):
  result = 0
  if num1 > num2:
    result = num1 - num2
  elif num1 < num2:
    result = num2 - num1
  else:
    result = num1 * num2
  return result