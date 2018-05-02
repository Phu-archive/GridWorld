# This file contain the defintion of the game class.


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

    def render_map(self):
        """
        Render the map y returning the numpy array

        Return
            Image (numpy array) - the entire map rendered to an image.
        """
