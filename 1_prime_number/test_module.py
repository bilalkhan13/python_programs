import importlib
import pytest
from isPrime import isPrime

test_cases = [
pytest.param( 25, "25 is not a prime number. Because it is divided by 5.", "Expected 25 is not a prime number. Because it is divided by 5.", id = "test not a prime number."),
pytest.param( 5, "5 is a prime number.", "Expected 25 is a prime number.", id = "test a prime number."),
pytest.param( -2, "-2 is not a prime number.", "Expected -2 is not a prime number.", id = "test not a prime number less than and equal to 1."),
]

@pytest.mark.parametrize('arguments,expected_output,fail_message', test_cases)
def test_template(arguments, expected_output, fail_message):
    actual = isPrime(arguments)
    assert actual == expected_output, fail_message