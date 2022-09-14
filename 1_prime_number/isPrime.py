def isPrime(integer_value):
  if integer_value > 1:
    for i in range(2, integer_value-1):
      if(integer_value % i == 0):
        return f"{integer_value} is not a prime number. Because it is divided by {i}."

    return f"{integer_value} is a prime number."
  else:
    return f"{integer_value} is not a prime number."