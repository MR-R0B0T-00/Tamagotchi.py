import schedule
import pyglet
from my_pet import Dog
from pyglet.window import key

window = pyglet.window.Window(300, 300, caption='Tamagotchi.py')
background = pyglet.resource.image('img/backgrounds/bg_main.png')
buttons_batch = pyglet.graphics.Batch()
pet = Dog('Korgy')
buttons_img = ['img/sprites/menu/status.png', 'img/sprites/menu/food.png',
               'img/sprites/menu/health.png', 'img/sprites/menu/enjoy.png',
               'img/sprites/menu/money.png']
buttons = [pyglet.image.load(img) for img in buttons_img]
status_sprite = pyglet.sprite.Sprite(buttons[0], x=8, y=250, batch=buttons_batch)
food_sprite = pyglet.sprite.Sprite(buttons[1], x=68, y=250, batch=buttons_batch)
health_sprite = pyglet.sprite.Sprite(buttons[2], x=128, y=250, batch=buttons_batch)
enjoy_sprite = pyglet.sprite.Sprite(buttons[3], x=188, y=250, batch=buttons_batch)
money_sprite = pyglet.sprite.Sprite(buttons[4], x=248, y=250, batch=buttons_batch)


# pyglet.font.add_file('fonts/pixeltiny.ttf')
# pixel_font = pyglet.font.load('PixelTiny')
# label_name = pyglet.text.Label(pet.name, x=window.width // 2, y=270, anchor_x='center',
#                                font_name='PixelTiny', font_size=70)


# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.LEFT:
#         pet_sprite.x -= 5
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        print(x, y)


window.push_handlers(on_mouse_press)


@window.event
def on_draw():
    window.clear()
    background.blit(0, 0)
    pet.sprite.draw()
    buttons_batch.draw()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(pet.update, interval=0.6)
    pyglet.app.run()
