import schedule
import pyglet
from pyglet.window import Window
from game_func import on_mouse_press, on_mouse_release, draw_sprites, update

window = Window(300, 300, caption='Tamagotchi.py')
background = pyglet.resource.image('img/backgrounds/bg_main.png')
window.push_handlers(on_mouse_press, on_mouse_release)


@window.event
def on_draw():
    window.clear()
    background.blit(0, 0)
    draw_sprites()


if __name__ == '__main__':
    update()
    pyglet.app.run()
