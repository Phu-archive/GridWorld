# Just an nothing object, that can't walk path.

from ..Prefabs import prefab, player
from abc import ABC, abstractmethod

class Static(prefab.Prefab):
    def __init__(self, color, size):
        super().__init__(color, size)
