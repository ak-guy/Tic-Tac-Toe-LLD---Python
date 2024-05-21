class NotEnoughPlayers(BaseException):
    def __init__(self, msg: str = 'There should be atleast 2 players to play the game'):
        self._msg = msg
