import model.calculator as calculator
import pytest

def test_add():
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0
    assert calculator.add(-1, -1) == -2


def test_minus():
    assert calculator.minus(2, 1) == 1
    assert calculator.minus(1, 2) == -1
    assert calculator.minus(-1, -1) == 0
    assert calculator.minus(0, 0) == 0


def test_power():
    assert calculator.power(2) == 4
    assert calculator.power(3) == 9
    assert calculator.power(-2) == 4
    assert calculator.power(0) == 0