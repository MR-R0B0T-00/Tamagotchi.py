import pyglet
from pyglet.window import Window
from game_func import main_batch, on_mouse_release, update_game, menu
from load_resources import background

window = Window(220, 220, caption='My PET')


@window.event
def on_draw():
    window.clear()
    background.blit(140, 100)
    main_batch.draw()
    menu.text_batch.draw()


window.push_handlers(on_mouse_release)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update_game, 1 / 3)
    pyglet.app.run()
