# Interactive Class.

from ..Prefabs import prefab
from abc import ABC, abstractmethod

class Interactive(prefab.Prefab):
    """
    Anything that can be Touch, Move, Eat. 
    """
    def __init__(self, color, size):
        super().__init__(color, size)
