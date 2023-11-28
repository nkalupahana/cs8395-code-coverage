def ex2(n):
  if n > 0:
    if n % 2 == 0: 
      result = n * 2
    else: 
      result = n + 1
  else:
    result = n - 1
  return result