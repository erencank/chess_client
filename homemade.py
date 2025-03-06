import random

import chess
from chess.engine import PlayResult

from libs.engine import MinimalEngine
from libs.handler import start_bot


class ExampleEngine(MinimalEngine):
    pass


class RandomMove(ExampleEngine):
    """The most simple engine, that picks a random move."""

    def search(self, board: chess.Board) -> PlayResult:
        move = random.choice(list(board.legal_moves))
        return PlayResult(move, None)


class Alphabetical(ExampleEngine):
    def search(self, board: chess.Board) -> PlayResult:
        moves = list(board.legal_moves)
        moves.sort(key=board.san)
        return PlayResult(moves[0], None)


class FirstMove(ExampleEngine):
    def search(self, board: chess.Board) -> PlayResult:
        moves = list(board.legal_moves)
        moves.sort(key=str)
        return PlayResult(moves[0], None)


class Homemade(ExampleEngine):
    def search(self, board: chess.Board) -> PlayResult:
        # Fill in your code here
        pass


if __name__ == "__main__":
    start_bot(engine=RandomMove())
