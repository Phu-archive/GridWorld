# This file contain the defintion of the game class.


class Game(object):
    def __init__(self, objs_lookup, objs_info, map_size):
        self.objs_lookup = objs_lookup
        self.objs_info = objs_info
        self.map_size = map_size
