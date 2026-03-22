from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import mouse, Entity, destroy

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.gravity = 0.5
        self.speed = 5
        self.jump_height = 4

        self.current_block_type = 'stone'

        self.block_types = ['grass', 'dirt', 'stone']
        
        self.block_models = {
            'grass': 'assets/textures/grass.png',
            'dirt': 'assets/textures/dirt.png',
            'stone': 'assets/textures/stone.png'
        }

    def input(self, key):
        super().input(key)

        if key == 'left mouse down':
            hit_info = mouse.hovered_entity
            if hit_info and hit_info != self:
                destroy(hit_info)

        elif key == 'right mouse down':
            hit_info = mouse.hovered_entity
            if hit_info:
                block_position = hit_info.position + mouse.normal
                Entity(
                    model='cube',
                    texture=self.block_models[self.current_block_type],
                    position=block_position,
                    collider='box'
                )

        elif key in ['1', '2', '3']:
            index = int(key) - 1
            self.current_block_type = self.block_types[index]
