def ex8(num1, num2):
  result = 0

  if num1 > num2:
    result = num1 + num2
  else:
    result = num1 - num2
  
  if result > 0:
    result = result * result
  else:
    result = result * 2
  
  return result