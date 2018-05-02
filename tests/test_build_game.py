from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from GridWorld import build_game
import pytest
from ..Prefabs import player, static

ascii_art_test = ['####',
                  '# P#',
                  '#  #',
                  '####']

obj_information_test = {
    'P': player.NormalPlayer((0, 255, 0), 2),
    '#': static.Static((0, 0, 0), 2)
}

def test_empty_map():
    expect_msg = "The map is empty"
    with pytest.raises(build_game.AsciiMapException) as excinfo:
        build_game.build_game([], {})

    assert expect_msg in str(excinfo.value)

def test_not_rectangle():
    expect_msg = "The map is not consistent"
    with pytest.raises(build_game.AsciiMapException) as excinfo:
        build_game.build_game(['      ', ' '], {})

    assert expect_msg in str(excinfo.value)

def test_element_not_in_object_information():
    expect_msg = "The object information is empty."
    with pytest.raises(build_game.ObjectInfoException) as excinfo:
        build_game.build_game(['    ', ' #  '], {})

    assert expect_msg in str(excinfo.value)


def test_element_not_in_object_information():
    expect_msg = "There is no information for the object."
    with pytest.raises(build_game.ObjectInfoException) as excinfo:
        build_game.build_game(['    ', ' #  '], {"?": static.Static((255, 0, 0), 2)})

    assert expect_msg in str(excinfo.value)

def test_too_much_information():
    expect_msg = "Some of the objects are not in the map."
    with pytest.raises(build_game.ObjectInfoException) as excinfo:
        build_game.build_game(['    ', '    '], {'#': static.Static((255, 0, 0), 2)})

    assert expect_msg in str(excinfo.value)

def test_finish_game():
    game = build_game.build_game(ascii_art_test, obj_information_test)

    expected_objs_look_up = {
        (0, 0): static.Static((0, 0, 0), 2),
        (1, 0): static.Static((0, 0, 0), 2),
        (2, 0): static.Static((0, 0, 0), 2),
        (3, 0): static.Static((0, 0, 0), 2),

        (0, 1): static.Static((0, 0, 0), 2),
        (3, 1): static.Static((0, 0, 0), 2),

        (0, 2): static.Static((0, 0, 0), 2),
        (3, 2): static.Static((0, 0, 0), 2),

        (0, 3): static.Static((0, 0, 0), 2),
        (1, 3): static.Static((0, 0, 0), 2),
        (2, 3): static.Static((0, 0, 0), 2),
        (3, 3): static.Static((0, 0, 0), 2),

        (2, 1): player.NormalPlayer((0, 255, 0), 2)
    }

    # Checking for types.
    assert len(game.objs_lookup.items()) == len(expected_objs_look_up.items())
    assert all(type(l) is type(e)
                for l, e in zip(game.objs_lookup.items(), expected_objs_look_up.items()))

    assert game.map_size == (4,4)
