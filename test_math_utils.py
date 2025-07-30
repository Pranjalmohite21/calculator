import pytest
from calculator import add, subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 5) == -5

def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(3, 2) == 1.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
