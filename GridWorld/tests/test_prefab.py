from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest
from GridWorld.Prefabs import prefab, exceptions

import numpy as np

@pytest.mark.parametrize("color_input, expect_msg", [
    ("Blue", "Expect 3 elements tuple - got str"),
    (102, "Expect 3 elements tuple - got int"),
    ([1, 2, 3], "Expect 3 elements tuple - got list")
])
def test_prefab_wrong_color_type(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab(color_input)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("color_input, expect_msg", [
    ((1, 2, 3, 4), "Expect 3 elements tuple - got 4 elements tuple"),
    ((), "Expect 3 elements tuple - got 0 elements tuple"),
])
def test_prefab_color_wrong_tuple_len(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab(color_input)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("color_input, expect_msg", [
    ((1, 2, None), "Expect 3 elements tuple of type int"),
    ((1, 2, "3"), "Expect 3 elements tuple of type int"),
    (("3", 4, 5), "Expect 3 elements tuple of type int")
])
def test_prefab_color_wrong_type_tuple(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab(color_input)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("color_input, expect_msg", [
    ((255, 255, -100), "Color can't be more than 255 or less than 0"),
    ((255, 0, 256), "Color can't be more than 255 or less than 0"),
    ((1, 260,-121), "Color can't be more than 255 or less than 0")
])
def test_prefab_color_wrong_type_tuple(color_input, expect_msg):
    with pytest.raises(ValueError) as execinfo:
        p = prefab.Prefab(color_input)

    assert expect_msg in str(execinfo.value)


@pytest.mark.parametrize("color_input, expect_msg", [
    ("Yellow", "Expect 3 elements tuple - got str"),
    ((1, 2, 3, 4), "Expect 3 elements tuple - got 4 elements tuple"),
    (("3", 4, 5), "Expect 3 elements tuple of type int")
])
def test_prefab_color_setter(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab((255, 255, 255))
        p.color = color_input

    assert expect_msg in str(execinfo.value)

def test_prefab_color_setter_success():
    p = prefab.Prefab((255, 255, 255))
    p.color = (200, 200, 200)

    assert p.color == (200, 200, 200)

@pytest.mark.parametrize("size_input, expect_msg", [
    ("10", "Expect size to be int - got str"),
    ([10], "Expect size to be int - got list"),
    (None, "Expect size to be int - got None")
])
def test_size_prefab_type(size_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab((255, 255, 255))
        p.size = size_input

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("size_input, expect_msg", [
    (0, "Expect size to be positive int"),
    (-10, "Expect size to be positive int")
])
def test_size_prefab_val(size_input, expect_msg):
    with pytest.raises(ValueError) as execinfo:
        p = prefab.Prefab((255, 255, 255))
        p.size = size_input

    assert expect_msg in str(execinfo.value)


def test_size_prefab_success():
    p = prefab.Prefab((255, 255, 255))
    p.size = 100

    assert p.size == 100


def test_create_numpy_tile():
    p = prefab.Prefab((255, 0, 0))
    p.size = 2

    tile_numpy_out = np.array([[[1, 0, 0], [1, 0, 0]],
                        [[1, 0, 0], [1, 0.0, 0]]])

    assert np.array_equal(p.numpy_tile, tile_numpy_out)

@pytest.fixture()
def normal_prefab():
    return prefab.Prefab((255, 0, 0))

@pytest.mark.parametrize("location_input, expect_msg", [
    ("Blue", "Expect 2 elements tuple - got str"),
    (102, "Expect 2 elements tuple - got int"),
    ([1, 2, 3], "Expect 2 elements tuple - got list")
])
def test_prefab_wrong_location_type(location_input, expect_msg, normal_prefab):
    with pytest.raises(TypeError) as execinfo:
        normal_prefab.location = location_input

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("location_input, expect_msg", [
    ((1, 2, 3, 4), "Expect 2 elements tuple - got 4 elements tuple"),
    ((), "Expect 2 elements tuple - got 0 elements tuple")
])
def test_prefab_wrong_location_size(location_input, expect_msg, normal_prefab):
    with pytest.raises(TypeError) as execinfo:
        normal_prefab.location = location_input

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("location_input, expect_msg", [
    ((1, "2"), "Expect 2 elements tuple of type int"),
    ((None, 2), "Expect 2 elements tuple of type int")
])
def test_prefab_wrong_location_not_int(location_input, expect_msg, normal_prefab):
    with pytest.raises(TypeError) as execinfo:
        normal_prefab.location = location_input

    assert expect_msg in str(execinfo.value)

def test_not_init_size(normal_prefab):
    expect_msg = "The size isn't initilized."
    with pytest.raises(exceptions.NotInitalizedException) as execinfo:
        a = normal_prefab.size

    assert expect_msg in str(execinfo.value)
