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
               'img/sprites/menu/money.png', 'img/sprites/menu/selected.png']
buttons = [pyglet.image.load(img) for img in buttons_img]

status_sprite = pyglet.sprite.Sprite(buttons[0], x=8, y=250, batch=buttons_batch)
food_sprite = pyglet.sprite.Sprite(buttons[1], x=68, y=250, batch=buttons_batch)
health_sprite = pyglet.sprite.Sprite(buttons[2], x=128, y=250, batch=buttons_batch)
enjoy_sprite = pyglet.sprite.Sprite(buttons[3], x=188, y=250, batch=buttons_batch)
money_sprite = pyglet.sprite.Sprite(buttons[4], x=248, y=250, batch=buttons_batch)
selected_sprite = pyglet.sprite.Sprite(buttons[5], x=-248, y=-250, batch=buttons_batch)

shape = pyglet.shapes.Rectangle(-300, -300, 282, 200, color=(0, 0, 200))
shape.opacity = 150


# pyglet.font.add_file('fonts/pixeltiny.ttf')
# pixel_font = pyglet.font.load('PixelTiny')
# label_name = pyglet.text.Label(pet.name, x=window.width // 2, y=270, anchor_x='center',
#                                font_name='PixelTiny', font_size=70)
def on_hint(self, x, y):
    if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
        return True
    else:
        return False


# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.LEFT:
#         pet_sprite.x -= 5
def on_mouse_press(x, y, button, modifiers):
    if on_hint(status_sprite, x, y):
        selected_sprite.x = status_sprite.x
        selected_sprite.y = status_sprite.y
        shape.x = 8
        shape.y = 45
    elif on_hint(food_sprite, x, y):
        selected_sprite.x = food_sprite.x
        selected_sprite.y = food_sprite.y
    elif on_hint(health_sprite, x, y):
        selected_sprite.x = health_sprite.x
        selected_sprite.y = health_sprite.y
    elif on_hint(enjoy_sprite, x, y):
        selected_sprite.x = enjoy_sprite.x
        selected_sprite.y = enjoy_sprite.y
    elif on_hint(money_sprite, x, y):
        selected_sprite.x = money_sprite.x
        selected_sprite.y = money_sprite.y


def on_mouse_release(x, y, button, modifiers):
    selected_sprite.x = -300


# def draw_status():
#     shape = pyglet.shapes.Rectangle(8, 45, 282, 200, color=(0, 0, 200))
#     shape.opacity = 150
#     shape.draw()


window.push_handlers(on_mouse_press, on_mouse_release)


@window.event
def on_draw():
    window.clear()
    background.blit(0, 0)
    pet.sprite.draw()
    buttons_batch.draw()
    shape.draw()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(pet.update, interval=0.6)
    pyglet.app.run()
