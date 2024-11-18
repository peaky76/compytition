from compytition import Outcome, OutcomeToPointsMapping


def test_outcome_to_points_mapping_uses_default_win():
    mapping = OutcomeToPointsMapping()
    assert mapping[Outcome.WIN] == 3

def test_outcome_to_points_mapping_uses_default_lose():
    mapping = OutcomeToPointsMapping()
    assert mapping[Outcome.LOSE] == 0

def test_outcome_to_points_mapping_uses_default_draw():
    mapping = OutcomeToPointsMapping()
    assert mapping[Outcome.DRAW] == 1

def test_outcome_to_points_mapping_custom_win():
    mapping = OutcomeToPointsMapping(win=5)
    assert mapping[Outcome.WIN] == 5

def test_outcome_to_points_mapping_custom_lose():
    mapping = OutcomeToPointsMapping(lose=-1)
    assert mapping[Outcome.LOSE] == -1

def test_outcome_to_points_mapping_custom_draw():
    mapping = OutcomeToPointsMapping(draw=2)
    assert mapping[Outcome.DRAW] == 2
