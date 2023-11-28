def ex4(num):
  if num % 2 == 0:
    if num % 4 == 0:
      num = num//4
    else:
      num = num//2
  return num