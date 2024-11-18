from compytition import Outcome


def test_outcome_win():
    assert Outcome.WIN
    assert Outcome.WIN.name == 'WIN'
    assert Outcome["WIN"] == Outcome.WIN

def test_outcome_lose():
    assert Outcome.LOSE
    assert Outcome.LOSE.name == 'LOSE'
    assert Outcome["LOSE"] == Outcome.LOSE

def test_outcome_draw():
    assert Outcome.DRAW
    assert Outcome.DRAW.name == 'DRAW'
    assert Outcome["DRAW"] == Outcome.DRAW


def test_outcome_win_shorthand():
    assert Outcome["W"] == Outcome.WIN

def test_outcome_lose_shorthand():
    assert Outcome["L"] == Outcome.LOSE

def test_outcome_draw_shorthand():
    assert Outcome["D"] == Outcome.DRAW

