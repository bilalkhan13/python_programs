def is_prime(input_value):
  if not input_value.isnumeric():
    return False

  integer = int(input_value)
  for i in range(2, integer-1):
    if(integer % i == 0):
      return False
  return True
