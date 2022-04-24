import pyglet
from pyglet.window import Window
from game_func import draw_sprites, update
from load_resources import background

window = Window(300, 300, caption='My PET')


@window.event
def on_draw():
    window.clear()
    background.blit(0, 0)
    draw_sprites()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 3)
    pyglet.app.run()
