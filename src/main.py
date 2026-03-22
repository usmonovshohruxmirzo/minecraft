from ursina import *
from environment import Environment
from player import Player
from world import World

app = Ursina()

Environment.init()

World.init()

player = Player(position=(0,2,0))

app.run()
