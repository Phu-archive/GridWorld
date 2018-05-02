# Player Prefab so that we can control it.
# from Prefabs import player, prefab
from ..Prefabs import prefab, player, exceptions
from abc import ABC, abstractmethod

class Player(prefab.Prefab):
    def __init__(self, color, size):
        super().__init__(color, size)
        self._location = None
        self._game = None

    @property
    def game(self):
        """Get the game object, will initilized this afterward"""
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        return self._game

    @game.setter
    def game(self, value):
        """Get the reference of the game, will initilized this afterward"""
        self._game = value

    @abstractmethod
    def step(self, action):
        """
        Given Action what should the player do?

        Arg:
            1. action (int) - The action we want the player to do.
        """
        pass

    def _north(self):
        """
        Move the player to the north direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_north(self.location)

    def _east(self):
        """
        Move the player to the east direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_east(self.location)

    def _south(self):
        """
        Move the player to the south direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_south(self.location)

    def _west(self):
        """
        Move the player to the west direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_west(self.location)

class NormalPlayer(Player):
    def __init__(self, color, size):
        super().__init__(color, size)

    def step(self, action):
        if action == 1:
            self._north()
        elif action == 2:
            self._east()
        elif action == 3:
            self._south()
        elif action == 4:
            self._west()
