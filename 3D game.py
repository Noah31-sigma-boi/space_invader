import ursina
from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

light = Entity()
DirectionalLight(parent=light, x=10,z=10,y=10, rotation=(45,45,0))

maze = Entity(model="plane", color=color.gray, shader=lit_with_shadows_shader, collider="mesh", scale=18)
Sky()

player=FirstPersonController(model="cube")
camera.z = -5
player.gravity = 0
if held_keys["e"]:
    print("eee")
player.speed = 10
app.run()

