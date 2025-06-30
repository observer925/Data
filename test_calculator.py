import pytest
from calculator import Calculator


def test_add():
    obj = Calculator(memory=0)
    obj.add(13)
    assert obj.memory == 13
    obj.add(1)
    assert obj.memory == 14


def test_sub():
    obj = Calculator(memory=1)
    obj.sub(3)
    assert obj.memory == -2


def test_mult():
    obj = Calculator(memory=7)
    obj.mult(5)
    assert obj.memory == 35


def test_div():
    obj = Calculator(memory=99)
    obj.div(9)
    assert obj.memory == 11
    with pytest.raises(ZeroDivisionError):
        obj.div(0)


def test_nth_root():
    obj = Calculator(memory=16)
    obj.nth_root(2)
    assert obj.memory == 4
    obj.memory = 27
    obj.nth_root(3)
    assert obj.memory == 3
    with pytest.raises(ZeroDivisionError):
        obj.nth_root(0)


def test_reset():
    """
    Should reset memory and operator
    """
    obj = Calculator(memory=12345, operator="/")
    obj.reset()
    assert obj.memory == 0
    assert obj.operator is None


def test_str():
    """
    If whole number, __str__ should return value as an integer.
    If float with a fraction, __str__ should round it to 2 decimals.
    """
    obj = Calculator(memory=5)
    assert str(obj) == "Current result: 5"
    obj.memory = 13.1234
    assert str(obj) == "Current result: 13.12"


def test_check_operator_and_operation():
    obj = Calculator(memory=33)
    obj.check_operator("/")
    obj.perform_operation(11)
    assert obj.memory == 3

    obj.check_operator("-")
    obj.perform_operation(3)
    assert obj.memory == 0


def test_invalid_operator():
    obj = Calculator()
    with pytest.raises(ValueError):
        obj.check_operator("Anything")
