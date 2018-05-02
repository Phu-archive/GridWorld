# Player Prefab so that we can control it.
# from Prefabs import player, prefab
from ..Prefabs import prefab, player
from abc import ABC, abstractmethod

class NotInitalizedException(Exception):
    pass

class Player(prefab.Prefab):
    def __init__(self, color, size):
        super().__init__(color, size)
        self._location = None
        self._game = None

    @property
    def location(self):
        """
        Get the location of the player.
        Noted that it will in initilized when create the map

        Return
            1. location (2 elements tuple) - the location of the player.
        """
        if self._location is None:
            raise NotInitalizedException("Location haven't been initilized")

        return self._location

    @location.setter
    def location(self, value):
        """
        Set the location of the player.
        Noted that it will in initilized when create the map

        Args:
            1. value (2 elements tuple) - the location of the player.

        Raises:
            TypeError - When the value contains non-integer values or
                the size of the tuple is not 2
        """

        # Similar to prefab
        if not isinstance(value, tuple):
            raise TypeError("Expect 2 elements tuple - got " +
                                    value.__class__.__name__)
        else:
            if len(value) != 2:
                raise TypeError("Expect 2 elements tuple - got " +
                                    str(len(value)) + " elements tuple.")
            elif not all(isinstance(c, int) for c in value):
                raise TypeError("Expect 2 elements tuple of type int")

        self._location = value

    @property
    def game(self):
        """Get the game object, will initilized this afterward"""
        if self._game is None:
            raise NotInitalizedException("Game haven't been initilized")

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
            raise NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_north(self.location)

    def _east(self):
        """
        Move the player to the east direction.
        """
        if self._game is None:
            raise NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_east(self.location)

    def _south(self):
        """
        Move the player to the south direction.
        """
        if self._game is None:
            raise NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_south(self.location)

    def _west(self):
        """
        Move the player to the west direction.
        """
        if self._game is None:
            raise NotInitalizedException("Game haven't been initilized")

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
