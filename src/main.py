from ursina import *
from player import Player
from world import World

app = Ursina()

World.init()

player = Player(position=(0,2,0))

app.run()
