# This file contain the defintion of the game class.

import numpy as np
import matplotlib.pyplot as plt
from Prefabs import exceptions, player, static, interactive

class Game(object):
    """
    Game Enviroment Class

    Attributes:
        objs_lookup (dict) - Getting the object based on the location.
        map_size (2 element tuple) - the size of the map (w x h)
    """
    def __init__(self, objs_lookup, map_size):
        self.objs_lookup = objs_lookup
        self.map_size = map_size

        # Just get the size of the object in the scene
        self._obj_size = list(self.objs_lookup.items())[0][1].size

        # Just create an object of the same size.
        _empty_tile = static.Static((255, 255, 255))
        _empty_tile.size = self._obj_size

        self.empty_tile_numpy = _empty_tile.numpy_tile

    def render_map(self):
        """
        Render the map y returning the numpy array

        Return
            Image (numpy array) - the entire map rendered to an image.
        """
        size_x, size_y = self.map_size
        map_array = []

        for x in range(size_x):
            row = []
            for y in range(size_y):
                if (x, y) in self.objs_lookup:
                    row.append(self.objs_lookup[(x,y)].numpy_tile)
                else:
                    row.append(self.empty_tile_numpy)
            # Have to reverse for the reshape to work.
            map_array.append(np.hstack(row))

        # Have to reverse for the reshape to work.
        image = np.array(map_array).reshape(size_x * self._obj_size,
                                                size_y * self._obj_size, 3)

        assert all(len(map_array[0]) == len(r) for r in map_array)

        # Flipping the image.
        return np.flip(np.rot90(image), 0)

    def display_map(self):
        """
        Display map of the game.
        """
        plt.imshow(self.render_map())
        plt.show()
