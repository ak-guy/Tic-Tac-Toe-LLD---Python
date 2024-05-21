from piece import PlayingPiece
class Player:
    def __init__(self, name: str, piece: PlayingPiece):
        self._name = name
        self._piece = piece

    @property
    def piece(self):
        return self._piece
    
    @piece.setter
    def piece(self, piece: PlayingPiece):
        self._piece = piece
