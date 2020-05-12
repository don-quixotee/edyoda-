from utilities import add
import pytest


@pytest.mark.mark1
def test_add3():
    result = add("python",109)
    assert result == "Invalid Input"