from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest
from ..Prefabs import prefab

import numpy as np
import matplotlib.pyplot as plt

@pytest.mark.parametrize("color_input, expect_msg", [
    ("Blue", "Expect 3 elements tuple - got str"),
    (102, "Expect 3 elements tuple - got int"),
    ([1, 2, 3], "Expect 3 elements tuple - got list")
])
def test_prefab_wrong_color_type(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab(color_input, 10)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("color_input, expect_msg", [
    ((1, 2, 3, 4), "Expect 3 elements tuple - got 4 elements tuple"),
    ((), "Expect 3 elements tuple - got 0 elements tuple"),
])
def test_prefab_color_wrong_tuple_len(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab(color_input, 10)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("color_input, expect_msg", [
    ((1, 2, None), "Expect 3 elements tuple of type int"),
    ((1, 2, "3"), "Expect 3 elements tuple of type int"),
    (("3", 4, 5), "Expect 3 elements tuple of type int")
])
def test_prefab_color_wrong_type_tuple(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab(color_input, 10)

    assert expect_msg in str(execinfo.value)


@pytest.mark.parametrize("color_input, expect_msg", [
    ("Yellow", "Expect 3 elements tuple - got str"),
    ((1, 2, 3, 4), "Expect 3 elements tuple - got 4 elements tuple"),
    (("3", 4, 5), "Expect 3 elements tuple of type int")
])
def test_prefab_color_setter(color_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab((255, 255, 255), 10)
        p.color = color_input

    assert expect_msg in str(execinfo.value)

def test_prefab_color_setter_success():
    p = prefab.Prefab((255, 255, 255), 10)
    p.color = (200, 200, 200)

    assert p.color == (200, 200, 200)

@pytest.mark.parametrize("size_input, expect_msg", [
    ("10", "Expect size to be int - got str"),
    ([10], "Expect size to be int - got list"),
    (None, "Expect size to be int - got None")
])
def test_size_prefab_type(size_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab((255, 255, 255), size_input)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("size_input, expect_msg", [
    (0, "Expect size to be positive int"),
    (-10, "Expect size to be positive int")
])
def test_size_prefab_val(size_input, expect_msg):
    with pytest.raises(ValueError) as execinfo:
        p = prefab.Prefab((255, 255, 255), size_input)

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("size_input, expect_msg", [
    (0, "Expect size to be positive int"),
    (-10, "Expect size to be positive int")
])
def test_size_prefab_val_setter(size_input, expect_msg):
    with pytest.raises(ValueError) as execinfo:
        p = prefab.Prefab((255, 255, 255), 10)
        p.size = size_input

    assert expect_msg in str(execinfo.value)

@pytest.mark.parametrize("size_input, expect_msg", [
    ("10", "Expect size to be int - got str"),
    ([10], "Expect size to be int - got list"),
    (None, "Expect size to be int - got None")
])
def test_size_prefab_type_setter(size_input, expect_msg):
    with pytest.raises(TypeError) as execinfo:
        p = prefab.Prefab((255, 255, 255), 10)
        p.size = size_input

    assert expect_msg in str(execinfo.value)


def test_size_prefab_success():
    p = prefab.Prefab((255, 255, 255), 10)
    p.size = 100

    assert p.size == 100


def test_create_numpy_tile():
    p = prefab.Prefab((255, 0, 0), 2)

    tile_numpy_out = np.array([[[1, 0, 0], [1, 0, 0]],
                        [[1, 0, 0], [1, 0.0, 0]]])

    assert np.array_equal(p.numpy_tile, tile_numpy_out)
