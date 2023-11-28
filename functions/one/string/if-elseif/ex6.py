def ex6(my_string):
  # Manipulate the string
  manipulated_string = my_string.lower()
  
  # Use if statement to check for specific conditions
  if 'a' in manipulated_string:
    return manipulated_string.upper()
  elif 'e' in manipulated_string:
    return manipulated_string.title()
  else:
    return manipulated_string
  
  # Return final result
  return manipulated_string