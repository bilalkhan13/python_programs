from unittest import main

def fibonacci_series(input_value):
  if not input_value.isnumeric():
    return "Please enter a valid number."

  integer = int(input_value)
  if integer == 0:
    return "Please enter a positive integer."

  if integer == 1:
    return "0"

  fibonacci_list = [0,1]
  count = 2

  while count < integer:
    fibonacci_list.append(fibonacci_list[count-2] + fibonacci_list[count-1])
    count = count + 1
  return fibonacci_list

main(module='test_module', exit=False)
print(fibonacci_series(input("Please enter a number: ")))