import importlib
import pytest
from is_prime import is_prime

test_cases = [
pytest.param( "25", False, "Expected Input should be a prime number.", id = "test not a prime number."),
pytest.param( "5", True, "Expected Input should be a prime number.", id = "test a prime number."),
pytest.param( "-2", False, "Expected Input should be a prime number.", id = "test not a prime number less than and equal to 1."),
pytest.param( "A", False, "Expected Input should be a number.", id = "test not a prime number less than and equal to 1."),
]

@pytest.mark.parametrize('arguments,expected_output,fail_message', test_cases)
def test_template(arguments, expected_output, fail_message):
    actual = is_prime(arguments)
    assert actual == expected_output, fail_message