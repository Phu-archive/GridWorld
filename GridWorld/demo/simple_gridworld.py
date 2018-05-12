import numpy as np
from GridWorld.build_game import build_game
from GridWorld.Prefabs import player, static, interactive

ascii_art_world = ['#####',
                   '# P #',
                   '# I #',
                   '#   #',
                   '#####']

class DemoPlayer(player.Player):
    def __init__(self, color):
        super().__init__(color)

    def step(self, action):
        """Only up and down movement"""
        if action == 0:
            self._north()
        elif action == 1:
            self._south()

class GoldObj(interactive.Interactive):
    def __init__(self, color):
        super().__init__(color)

    def touch(self, env):
        env.add_reward(100)

    def consume(self, env):
        """Still Under developement"""

obj_information= {
    'P': DemoPlayer((0, 0, 255)),
    '#': static.Static((0, 0, 0)),
    'I': GoldObj((0, 255, 0))
}

env = build_game(ascii_art_world, obj_information, 2)
obs = env.reset()
env.display_map()

obs, reward, done = env.step(1)
print("Reward is {}".format(reward))
env.display_map()

obs, reward, done = env.step(1)
env.display_map()
