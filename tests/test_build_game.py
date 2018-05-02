from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from GridWorld import build_game
import pytest
from ..Prefabs import prefab

ascii_art_test = [ '########'
                 , '#      #'
                 , '#      #'
                 , '#   P  #'
                 , '#      #'
                 , '#      #'
                 , '#      #'
                 , '########']

obj_information_test = {
    "#": prefab.Prefab((255, 0, 0), 2),
    "P": prefab.Prefab((255, 0, 0), 2)
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
        build_game.build_game(['    ', ' #  '], {"?": prefab.Prefab((255, 0, 0), 2)})

    assert expect_msg in str(excinfo.value)

def test_too_much_information():
    expect_msg = "Some of the objects are not in the map."
    with pytest.raises(build_game.ObjectInfoException) as excinfo:
        build_game.build_game(['    ', '    '], {'#': prefab.Prefab((255, 0, 0), 2)})

    assert expect_msg in str(excinfo.value)

def test_finish_game():
    game = build_game.build_game(ascii_art_test, obj_information_test)
    assert build_game.layers == expected_layers
