import pytest

from compytition.rank import Rank
from compytition.rank_list import RankList


def test_class_list_can_be_initialised_with_valid_tuple_of_ints():
    assert RankList((1, 2, 3))

def test_class_list_can_be_initialised_with_valid_list_of_ints():
    assert RankList([1, 2, 3])

def test_class_list_can_be_initialised_with_valid_tuple_of_equal_ints():
    assert RankList((1, 1, 3))

def test_class_list_can_be_initialised_with_valid_list_of_equal_ints():
    assert RankList([1, 1, 3])

def test_class_list_can_be_initialised_with_valid_tuple_of_strings():
    assert RankList(('1', '2', '3'))

def test_class_list_can_be_initialised_with_valid_list_of_strings():
    assert RankList(['1', '2', '3'])
    
def test_class_list_can_be_initialised_with_valid_tuple_of_equal_signed_strings():
    assert RankList(('1=', '1=', '3'))

def test_class_list_can_be_initialised_with_valid_list_of_equal_signed_strings():
    assert RankList(['1=', '1=', '3'])

def test_class_list_can_be_initialised_with_valid_tuple_of_ranks():
    assert RankList((Rank(1), Rank(2), Rank(3)))

def test_class_list_can_be_initialised_with_valid_list_of_ranks():
    assert RankList([Rank(1), Rank(2), Rank(3)])

def test_class_list_errors_if_initialised_with_invalid_sequence_of_ints():
    with pytest.raises(ValueError, match="Ranks must"):
        RankList((1, 2, 4))

def test_class_list_errors_if_initialised_with_invalid_sequence_of_equal_signed_strings():
    with pytest.raises(ValueError, match="Ranks must"):
        RankList(('1=', '1=', '2')) 