from typing import Any

from .rank import Rank


class Ranking(dict):
    def __init__(self, ranking: dict[Any, int | str | Rank]) -> None:
        for k, v in ranking.items():
            if not isinstance(v, (int, str, Rank)):
                raise ValueError(f"Invalid value for {k}: {v}")

        super().__init__({k: Rank(v) for k, v in ranking.items()})