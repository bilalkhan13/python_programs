from is_prime import is_prime
from pytest import main

main(['-vv'])
number = input("Please enter a prime number:")
print(is_prime(number))