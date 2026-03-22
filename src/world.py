from ursina import *

class World:
    @staticmethod
    def init():
        for x in range(-10, 10):
            for z in range(-10, 10):
                Entity(
                    model='cube',
                    texture="assets/textures/grass.png",
                    position=Vec3(x, 0, z),
                    collider='box'
                )
