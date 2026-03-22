from ursina import *
from player import Player

app = Ursina()

ground = Entity(
    model="plane",
    scale=(200, 20, 200),
    color=color.green,
    collider="mesh",
)

player = Player(position=(0,2,0))

app.run()
