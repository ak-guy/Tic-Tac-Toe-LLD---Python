from board import Board
from typing import List
from player import Player
from exceptions import *

class Game:
    def __init__(self, size: int):
        self.size = size
        self._board = Board(self.size)
        self._players: List[Player] = []
    
    def addPlayer(self, player: Player):
        self._players.append(player)

    def startGame(self):
        if len(self._players) <= 1:
            raise NotEnoughPlayers
        
        end_game = False
        winner = 'Tie'

        while not end_game:
            pass
