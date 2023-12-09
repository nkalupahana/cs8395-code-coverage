def ex0(num1, num2):
  if num1 > 0:
    if num2 > 0:
      result = num1 + num2
    else:
      result = num1 - num2
  else:
    if num2 > 0:
      result = num1 * num2
    else:
      result = num1 / num2
  return result