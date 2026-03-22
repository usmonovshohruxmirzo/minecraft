from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(
    model="plane",
    scale=(200, 20, 200),
    color=color.green,
    collider="mesh",
)

player = FirstPersonController()

app.run()
