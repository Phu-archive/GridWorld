from GridWorld import game, build_game
import numpy as np
from Prefabs import *

# Using the same game
ascii_art_test = ['####',
                  '# P#',
                  '#  #',
                  '####']
                  
ascii_art_test2 = ['########'
                  ,'#   P  #'
                  ,'#      #'
                  ,'#      #'
                  ,'#      #'
                  ,'#      #'
                  ,'#    A #'
                  ,'########']

obj_information_test = {
    'P': player.NormalPlayer((0, 0, 255)),
    '#': static.Static((0, 0, 0))
}

obj_information_test2 = {
    'P': player.NormalPlayer((0, 0, 255)),
    '#': static.Static((0, 0, 0)),
    'A': static.Static((0, 255, 0))
}

def test_render_map():
    g = build_game.build_game(ascii_art_test, obj_information_test, 2)
    img = g.render_map()
    g.display_map()

    assert img.shape == (8, 8, 3)
