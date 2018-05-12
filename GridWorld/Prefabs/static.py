# Just an nothing object, that can't walk path.

from GridWorld.Prefabs import prefab
from abc import ABC, abstractmethod

class Static(prefab.Prefab):
    """
    Static Prefab - Anything that can't be moved, or interact.
    """
    def __init__(self, color):
        super().__init__(color)
