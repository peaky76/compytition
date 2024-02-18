from typing import Any

from .rank import Rank


class Ranking(dict):
    def __init__(self, ranking: dict[Any, int | str | Rank]) -> None:        
        ranking = {k: Rank(v) for k, v in ranking.items()}

        previous_rank = 0
        tied = 0
        for rank in sorted(ranking.values(), reverse=True):
            current_rank = rank
            if int(current_rank) == int(previous_rank):
                tied += 1
            else:
                if int(previous_rank) + 1 + tied != int(current_rank):
                    message = "Ranks must be consecutive" if tied == 0 else "Ranks must account for ties"
                    raise ValueError(message)
                tied = 0
            previous_rank = current_rank
        
        super().__init__(ranking)