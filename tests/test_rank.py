import pytest

from compytition import Rank


def test_rank_can_be_initialised_with_int():
    assert Rank(1)

def test_rank_can_be_initialised_with_str():
    assert Rank('1')

def test_rank_can_be_initialised_with_equal_sign_after():
    assert Rank('1=')

def test_rank_can_be_initialised_with_equal_sign_before():
    assert Rank('=1')

def test_rank_can_be_initialised_with_tied_keyword():
    assert Rank(1, tied=True)

def test_rank_cannot_be_initialised_with_float():
    with pytest.raises(ValueError):  # noqa: PT011 until upgrade to peak_utility 0.6.1
        Rank(1.0)

def test_rank_cannot_be_initialised_with_invalid_string():
    with pytest.raises(ValueError):  # noqa: PT011 until upgrade to peak_utility 0.6.1
        Rank('a')

def test_rank_repr_when_not_tied():
    assert repr(Rank(1)) == '1st'

def test_rank_repr_when_tied():
    assert repr(Rank(1, tied=True)) == '1st='

def test_rank_str_when_not_tied():
    assert str(Rank(1)) == '1'

def test_rank_str_when_tied():
    assert str(Rank(1, tied=True)) == '1='

def test_rank_can_be_compared():
    assert Rank(1) > Rank(2)


