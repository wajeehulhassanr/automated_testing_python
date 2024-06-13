# test_math_operations.py

import pytest
from src.math_ops.math_ops import add, subtract, multiply, divide, sqrt

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    with pytest.raises(ValueError):
        divide(10, 0)

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    with pytest.raises(ValueError):
        sqrt(-1)
