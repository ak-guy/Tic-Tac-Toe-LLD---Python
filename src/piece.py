from __future__ import annotations
from enum import Enum

class PlayingPiece:
    def __init__(self, piece_type: PieceType):
        self._piecetype = piece_type

class PlayingPieceX(PlayingPiece):
    def __init__(self, piece_type: PieceType) -> PlayingPiece:
        super().__init__(piece_type=PieceType.X)

class PlayingPieceo(PlayingPiece):
    def __init__(self, piece_type: PieceType) -> PlayingPiece:
        super().__init__(piece_type=PieceType.O)

class PlayingPieceAtTheRate(PlayingPiece):
    def __init__(self, piece_type: PieceType) -> PlayingPiece:
        super().__init__(piece_type=PieceType.ATTHERATE)

class PlayingPieceHash(PlayingPiece):
    def __init__(self, piece_type: PieceType) -> PlayingPiece:
        super().__init__(piece_type=PieceType.HASH)

class PieceType(Enum):
    X = 'X'
    O = 'O'
    ATTHERATE = '@'
    HASH = '#'