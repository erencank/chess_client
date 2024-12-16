import chess
from chess.engine import PlayResult


class MinimalEngine:
    """
    A base class for homemade engines. Users should subclass this and implement `search`.
    """

    def search(self, board: chess.Board) -> PlayResult:
        raise NotImplementedError("Subclasses must implement search method.")
