import pytest

from ex113 import is_divisible


def test_divisible_numbers(self):
    assert is_divisible(10, 2) is True
    assert is_divisible(10, 10) is True
    assert is_divisible(10, 1) is True
        
def test_not_divisible_numbers(self):
    assert is_divisible(5, 3) is False
    assert is_divisible(5, 6) is False
    assert is_divisible(10, 3) is False

def test_divide_by_0(self):
    with pytest.raises(ZeroDivisionError):
        is_divisible(1, 0)