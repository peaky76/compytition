import pytest

from compytition import Rank


def test_rank_can_be_initialised_with_int():
    assert Rank(1)

def test_rank_can_be_initialised_with_str():
    assert Rank('1')

def test_rank_can_be_initialised_with_equal_sign():
    assert Rank('1=')

def test_rank_can_be_initialised_with_tied_keyword():
    assert Rank(1, tied=True)

def test_rank_cannot_be_initialised_with_float():
    with pytest.raises(ValueError):  # noqa: PT011
        Rank(1.0)

def test_rank_cannot_be_initialised_with_invalid_string():
    with pytest.raises(ValueError):  # noqa: PT011
        Rank('a')
