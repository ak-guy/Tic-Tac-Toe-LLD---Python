from piece import PlayingPiece
from __future__ import annotations
from typing import (
    List,
    Union
)

class Board:
    def __init__(self, size: int):
        self._board_size = size
        self.board: List[List[Union[PlayingPiece, str]]] = [['' for i in range(self._board_size)] for j in range(self._board_size)]

    def addPiece(self, row: int, col: int, playing_piece: PlayingPiece) -> bool:
        if self.board[row][col] != '':
            return False
        
        self.board[row][col] = playing_piece._piecetype.value
        return True