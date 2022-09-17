import unittest
from fibonacci_series import fibonacci_series

class UnitTests(unittest.TestCase):
  def test_not_a_number(self):
    actual = fibonacci_series("a")
    expected = "Please enter a valid number."
    self.assertEqual(actual, expected, 'Expected calling "fibonacci_series()" with "a", to return "Please enter a valid number."')

  def test_a_negative_input(self):
    actual = fibonacci_series("-2")
    expected = "Please enter a valid number."
    self.assertEqual(actual, expected, 'Expected calling "fibonacci_series()" with "-2", to return "Please enter a positive integer."')

  def test_a_value_0(self):
    actual = fibonacci_series("0")
    expected = "Please enter a positive integer."
    self.assertEqual(actual, expected, 'Expected calling "fibonacci_series()" with "0", to return "Please enter a positive integer."')

  def test_a_value_1(self):
    actual = fibonacci_series("1")
    expected = "0"
    self.assertEqual(actual, expected, 'Expected calling "fibonacci_series()" with "1", to return "1"')

  def test_a_positive_integer(self):
    actual = fibonacci_series("10")
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    self.assertEqual(actual, expected, 'Expected calling "fibonacci_series()" with "10", to return "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]""')

if __name__ == "__fibonacci_series__":
    unittest.main()