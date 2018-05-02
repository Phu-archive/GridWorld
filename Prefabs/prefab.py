# Base Case for the prefab objects in the game

from abc import ABC, abstractmethod
import numpy as np

import matplotlib.pyplot as plt

class Prefab(object):
    """
    Base Class for all prefabs(object) in the game.

    Attributes:
        color (3 elements tuple of ints) - the RGB code for the color.
            (range is 0-255 not 0-1)
        size (int) - the size of the pixel tile.

    Raises:
        TypeError -
            When the color type is not 3 elements integer tuple.
            When size is not int and not positive.
    """
    def __init__(self, color, size):
        self.color = color
        self.size = size

    @property
    def color(self):
        """Getter method for the color."""
        return self._color

    @color.setter
    def color(self, value):
        """
        Setter method for the color

        Args:
            value (3 element tuple) - the RGB code for the color.

        Raises:
            TypeError -
                If the value is not a tuple.
                If the size of the tuple is not 3.
                If the tuple doesn't contain integer.
        """
        if not isinstance(value, tuple):
            raise TypeError("Expect 3 elements tuple - got " +
                                    value.__class__.__name__)
        else:
            if len(value) != 3:
                raise TypeError("Expect 3 elements tuple - got " +
                                    str(len(value)) + " elements tuple.")
            if not all(isinstance(c, int) for c in value):
                raise TypeError("Expect 3 elements tuple of type int")

        self._color = value

    @property
    def size(self):
        """Getter method for the size"""
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for the size

        Args:
            value (positive int) - the size of the tile in the grid.

        Raises:
            TypeError - When the size is not int.
            ValueError - When the size is not positive.
        """

        if not isinstance(value, int):
            raise TypeError("Expect size to be int - got " +
                                value.__class__.__name__)
        else:
            if value <= 0:
                raise ValueError("Expect size to be positive int")

        self._size = value

    @property
    def numpy_tile(self):
        """
        Create the numpy tile for creating the grid world

        Return:
            numpy tile (size x size x 3 numpy array) - numpy tile
        """
        one_pixel = np.array([c/255 for c in self._color])
        tile_pixel = [[one_pixel for _ in range(self._size)]
                                    for _ in range(self._size)]
        return np.array(tile_pixel, dtype=np.float32)

    def _display_tile(self):
        """
        Display the tile. Use for debug only.
        """
        plt.imshow(self.numpy_tile)
        plt.show()
