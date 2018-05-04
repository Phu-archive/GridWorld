from GridWorld import game, build_game
import numpy as np
from Prefabs import *

import pytest

# Using the same game
ascii_art_test = ['####',
                  '#  #',
                  '# P#',
                  '####']

ascii_art_test2 = ['########'
                  ,'#      #'
                  ,'#      #'
                  ,'#      #'
                  ,'#      #'
                  ,'#    P #'
                  ,'#    A #'
                  ,'########']


ascii_art_test3 = ['####',
                   '# I#',
                   '# P#',
                   '####']

obj_information_test = {
    'P': player.NormalPlayer((0, 0, 255)),
    '#': static.Static((0, 0, 0))
}

obj_information_test2 = {
    'P': player.NormalPlayer((0, 0, 255)),
    '#': static.Static((0, 0, 0)),
    'A': static.Static((0, 255, 0))
}


obj_information_test3 = {
    'P': player.NormalPlayer((0, 0, 255)),
    '#': static.Static((0, 0, 0)),
    'I': interactive.Touchable((255, 0, 0))  
}

        
@pytest.fixture
def big_game():
    return build_game.build_game(ascii_art_test2, obj_information_test2, 2)

@pytest.fixture
def game():
    return build_game.build_game(ascii_art_test, obj_information_test, 2)

def test_render_map(game):
    img = game.render_map()
    # g.display_map()

    assert img.shape == (8, 8, 3)

@pytest.mark.parametrize("action, expect_location", [
    (1, (2, 1)),
    (2, (2, 2)),
    (3, (2, 2)),
    (4, (1, 2))
])

def test_player_moving(action, expect_location, game):
    obs = game.step(action)

    # Checking for types.
    # Not sure why the dict comparison doesn't work here.
    # assert expected_objs_look_up == game.objs_lookup

    # game.display_map()

    # so just check that the location is in
    assert expect_location in game.objs_lookup
    assert isinstance(game.objs_lookup[expect_location][0], player.Player)

    assert obs.shape == (8, 8, 3)

@pytest.mark.parametrize("action, expect_location", [
    (1, (5, 4)),
    (2, (6, 5)),
    (3, (5, 5)),
    (4, (4, 5))
])

def test_player_moving_big_map(action, expect_location, big_game):
    obs = big_game.step(action)

    # Checking for types.
    # Not sure why the dict comparison doesn't work here.
    # assert expected_objs_look_up == game.objs_lookup

    # big_game.display_map()

    # so just check that the location is in
    assert expect_location in big_game.objs_lookup
    assert isinstance(big_game.objs_lookup[expect_location][0], player.Player)

    assert obs.shape == (16, 16, 3)


def test_player_moving_in_obj(capsys):
   game = build_game.build_game(ascii_art_test3, obj_information_test3, 2)
   game.step(1)

   expect_loc = (2, 1)
   assert expect_loc in game.objs_lookup

   # Expect that the object lookup will have length 2.
   assert len(game.objs_lookup[expect_loc]) == 2

   # Test that the touch is called. 
   out = capsys.readouterr()
   # Since we copy every obj in the world we have to capture the touched instead
   assert out == "I am touched"

