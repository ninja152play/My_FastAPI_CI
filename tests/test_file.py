import pytest

from file import result_two


def test_func():
    result = result_two(5, 20)
    assert result == 25
