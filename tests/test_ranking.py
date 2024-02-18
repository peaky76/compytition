import pytest

from compytition import Rank, Ranking


def test_ranking_can_be_initialised_with_dict_of_objects_and_ints():
    assert Ranking({'a': 1, 'b': 2, 'c': 3})

def test_ranking_can_be_initialised_with_dict_of_objects_and_strs():
    assert Ranking({'a': '1', 'b': '2', 'c': '3=', 'd': '3='})

def test_ranking_can_be_initialised_with_dict_of_objects_and_ranks():
    assert Ranking({'a': Rank(1), 'b': Rank(2), 'c': Rank(3, tied=True), 'd': Rank(3, tied=True)})

def test_ranking_cannot_be_initialised_with_invalid_dict():
    with pytest.raises(ValueError):  # noqa: PT011 until upgrade to peak_utility 0.6.1
        Ranking({'a': "winner", 'b': 2.0, 'c': 3})

def test_ranking_cannot_be_initialised_with_non_consecutive_ranks():
    with pytest.raises(ValueError): # noqa: PT011 until upgrade to peak_utility 0.6.1
        Ranking({'a': 1, 'b': 3, 'c': 4})

def test_ranking_cannot_be_initialised_with_consecutive_int_ranks_after_tied():
    with pytest.raises(ValueError):  # noqa: PT011 until upgrade to peak_utility 0.6.1
        Ranking({'a': 1, 'b': 2, 'c': 2, 'd': 3})

def test_ranking_cannot_be_initialised_with_consecutive_obj_ranks_after_tied():
    with pytest.raises(ValueError):  # noqa: PT011 until upgrade to peak_utility 0.6.1
        Ranking({'a': Rank(1), 'b': Rank(2), 'c': Rank(2), 'd': Rank(3)})