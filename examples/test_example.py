"""Basic Unit testing for example.py"""
from random import randint
import pytest
from example import increment, COLORS

def test_increment():
    """Testing increment function"""
    test_value = randint(0,10)
    assert increment(3) == 4
    assert increment(-2) == -1
    assert increment(test_value) == test_value + 1

    for i in range(100):
        i = randint(1, 1000)
        assert increment(i-1) == i


def test_number_colors():
    """Testing colors contents"""
    assert len(COLORS) == 4


def test_color_contents():
    """Check for specific colors in the list"""
    assert "blue" in COLORS
    assert "brown" in COLORS
    assert "mauve" in COLORS