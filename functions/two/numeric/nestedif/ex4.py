def ex4(num1, num2):
  if num1 > 0 and num2 > 0:
    result = num1**2 + num2**2
  else:
    if num1 < 0 and num2 < 0:
      result = num1**3 + num2**3
    else:
      result = num1 + num2
  return result