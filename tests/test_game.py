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

ascii_art_test4 = ['####',
                   '# E#',
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

obj_information_test4 = {
    'P': player.NormalPlayer((0, 0, 255)),
    '#': static.Static((0, 0, 0)),
    'E': interactive.TouchableEnd((255, 0, 0))  
}

        
@pytest.fixture
def big_game():
    return build_game.build_game(ascii_art_test2, obj_information_test2, 2)

@pytest.fixture
def normal_game():
    return build_game.build_game(ascii_art_test, obj_information_test, 2)

@pytest.fixture
def touch_game():
    return build_game.build_game(ascii_art_test3, obj_information_test3, 2)

@pytest.fixture
def terminate_game():
    return build_game.build_game(ascii_art_test4, obj_information_test4, 2)

def test_render_map(normal_game):
    game = normal_game
    img = game.render_map()
    # g.display_map()

    assert img.shape == (8, 8, 3)

@pytest.mark.parametrize("action, expect_location", [
    (1, (2, 1)),
    (2, (2, 2)),
    (3, (2, 2)),
    (4, (1, 2))
])

def test_player_moving(action, expect_location, normal_game):
    game = normal_game
    obs, reward, terminate = game.step(action)

    # Checking for types.
    # Not sure why the dict comparison doesn't work here.
    # assert expected_objs_look_up == game.objs_lookup

    # game.display_map()

    # so just check that the location is in
    assert expect_location in game.objs_lookup
    assert isinstance(game.objs_lookup[expect_location][0], player.Player)

    assert obs.shape == (8, 8, 3)
    assert reward == 0
    assert terminate == False

@pytest.mark.parametrize("action, expect_location", [
    (1, (5, 4)),
    (2, (6, 5)),
    (3, (5, 5)),
    (4, (4, 5))
])

def test_player_moving_big_map(action, expect_location, big_game):
    obs, reward, terminate = big_game.step(action)

    # Checking for types.
    # Not sure why the dict comparison doesn't work here.
    # assert expected_objs_look_up == game.objs_lookup

    # big_game.display_map()

    # so just check that the location is in
    assert expect_location in big_game.objs_lookup
    assert isinstance(big_game.objs_lookup[expect_location][0], player.Player)

    assert obs.shape == (16, 16, 3)
    assert reward == 0
    assert terminate == False


def test_player_moving_in_obj(capsys, touch_game):
   game = touch_game
   game.step(1)

   expect_loc = (2, 1)
   assert expect_loc in game.objs_lookup

   # Expect that the object lookup will have length 2.
   assert len(game.objs_lookup[expect_loc]) == 2

   # Test that the touch is called. 
   out = capsys.readouterr()
   # Since we copy every obj in the world we have to capture the touched instead
   assert "I am Touched" in str(out)

def test_player_moving_in_obj_out(capsys, touch_game):
   game = touch_game
   game.step(1)

   expect_loc = (2, 1)
   assert expect_loc in game.objs_lookup

   # Expect that the object lookup will have length 2.
   assert len(game.objs_lookup[expect_loc]) == 2

   # Test that the touch is called. 
   out = capsys.readouterr()
   # Since we copy every obj in the world we have to capture the touched instead
   assert "I am Touched" in str(out)
   # Move out 
   game.step(3)
   new_expect_loc = (2, 2)
   
   assert new_expect_loc in game.objs_lookup
   assert len(game.objs_lookup[new_expect_loc]) == 1
   assert len(game.objs_lookup[expect_loc]) == 1

@pytest.mark.parametrize("reward", [
    "1",
    None
])

def test_reward(reward, normal_game):
    game = normal_game
    expect_msg = "The reward should be int, or float"

    with pytest.raises(TypeError) as excinfo:
        game.reward = reward

    assert expect_msg in str(excinfo.value)

@pytest.mark.parametrize("terminate", [
    "1",
    None,
    1
])
def test_terminate(terminate, normal_game):
    game = normal_game
    expect_msg = "Termination should be boolean"

    with pytest.raises(TypeError) as excinfo:
        game.terminate = terminate

    assert expect_msg in str(excinfo.value)

def test_player_moving_in_obj_reward(capsys, touch_game):
   game = touch_game
   observation, reward, terminate = game.step(1)

   expect_loc = (2, 1)
   assert expect_loc in game.objs_lookup

   # Expect that the object lookup will have length 2.
   assert len(game.objs_lookup[expect_loc]) == 2

   # Test that the touch is called. 
   out = capsys.readouterr()
   # Since we copy every obj in the world we have to capture the touched instead
   assert "I am Touched" in str(out)
   assert reward == 1

def test_player_touch_obj_terminate(capsys, terminate_game):
    # Move Up
    obs, reward, terminate = terminate_game.step(1)

    # it should get reward and terminate
    assert obs.shape == (8, 8, 3)
    assert reward == 1
    assert terminate
    
    # If we try to move up we should expect and error 
    expect_answer = "The env is terminated."
    with pytest.raises(exceptions.EnvTerminateException) as excinfo:
        obs, reward, terminate = terminate_game.step(2)
    assert expect_answer == str(excinfo.value)
                
