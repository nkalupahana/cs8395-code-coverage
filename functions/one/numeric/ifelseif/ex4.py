def ex4(n):
  if n % 2 == 0:
    return n + 10
  elif n % 3 == 0:
    return n * 10
  else:
    return n - 10
    
print(ex4(10)) #output: 20