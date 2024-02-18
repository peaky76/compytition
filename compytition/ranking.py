from typing import Any

from .rank import Rank


class Ranking(dict):
    def __init__(self, ranking: dict[Any, int | str | Rank]) -> None:        
        ranking = {k: Rank(v) for k, v in ranking.items()}
        
        super().__init__(ranking)