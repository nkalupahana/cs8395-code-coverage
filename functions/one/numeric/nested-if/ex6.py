def ex6(n):
  if n > 0:
    if n % 2 == 0:
      n = n/2
    else:
      n = n*3
  else:
    n = 0
  return n