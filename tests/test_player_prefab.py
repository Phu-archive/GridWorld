from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest
from ..Prefabs import player, prefab

import numpy as np

class GameMock:
    """Simple Game Mock Testing How the method calls"""
    def __init__(self):
        # Will tell which method is called in order.
        self.call_done = [False, False, False, False]

    def move_north(self, *args, **kwargs):
        self.call_done[0] = True
        return (0, 1)

    def move_east(self, *args, **kwargs):
        self.call_done[1] = True
        return (0, 1)

    def move_south(self, *args, **kwargs):
        self.call_done[2] = True
        return (0, 1)

    def move_west(self, *args, **kwargs):
        self.call_done[3] = True
        return (0, 1)

    def assert_call_order(self, calls_need):
        assert calls_need == self.call_done

@pytest.fixture()
def normal_player():
    return player.NormalPlayer((255, 0, 0), 2)

@pytest.mark.parametrize("location_input, expect_msg", [
    ("Blue", "Expect 2 elements tuple - got str"),
    (102, "Expect 2 elements tuple - got int"),
    ([1, 2, 3], "Expect 2 elements tuple - got list")
])
def test_player_wrong_location_type(location_input, expect_msg, normal_player):
    with pytest.raises(TypeError) as execinfo:
        normal_player.location = location_input

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("location_input, expect_msg", [
    ((1, 2, 3, 4), "Expect 2 elements tuple - got 4 elements tuple"),
    ((), "Expect 2 elements tuple - got 0 elements tuple")
])
def test_player_wrong_location_size(location_input, expect_msg, normal_player):
    with pytest.raises(TypeError) as execinfo:
        normal_player.location = location_input

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("location_input, expect_msg", [
    ((1, "2"), "Expect 2 elements tuple of type int"),
    ((None, 2), "Expect 2 elements tuple of type int")
])
def test_player_wrong_location_not_int(location_input, expect_msg, normal_player):
    with pytest.raises(TypeError) as execinfo:
        normal_player.location = location_input

    assert expect_msg in str(execinfo.value)

def test_player_location_not_initilized(normal_player):
    expect_msg = "Location haven't been initilized"
    with pytest.raises(player.NotInitalizedException) as execinfo:
        a = normal_player.location

    assert expect_msg in str(execinfo.value)

def test_player_game_not_initilized(normal_player):
    expect_msg = "Game haven't been initilized"
    with pytest.raises(player.NotInitalizedException) as execinfo:
        a = normal_player.game

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("action", [
    (1), (2), (3), (4)
])
def test_player_action(action, normal_player):
    expect_msg = "Game haven't been initilized"
    with pytest.raises(player.NotInitalizedException) as execinfo:
        a = normal_player.step(action)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("action, calls_need", [
    (1, [True, False, False, False]),
    (2, [False, True, False, False]),
    (3, [False, False, True, False]),
    (4, [False, False, False, True])
])
def test_player_call_count(action, normal_player, calls_need):
    game = GameMock()

    normal_player.game = game
    normal_player.location = (0, 0)

    a = normal_player.step(action)
    game.assert_call_order(calls_need)
