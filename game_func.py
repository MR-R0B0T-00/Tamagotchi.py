import pyglet
import animals
from pyglet.sprite import Sprite
from status_view import Status

pet = animals.Dog('Korgy')
status_name = Status(pet)

buttons_batch = pyglet.graphics.Batch()
buttons_img = ['img/sprites/menu/status.png', 'img/sprites/menu/food.png',
               'img/sprites/menu/health.png', 'img/sprites/menu/enjoy.png',
               'img/sprites/menu/money.png', 'img/sprites/menu/selected.png']
buttons = [pyglet.image.load(img) for img in buttons_img]

status_sprite = Sprite(buttons[0], x=8, y=250, batch=buttons_batch)
food_sprite = Sprite(buttons[1], x=68, y=250, batch=buttons_batch)
health_sprite = Sprite(buttons[2], x=128, y=250, batch=buttons_batch)
enjoy_sprite = Sprite(buttons[3], x=188, y=250, batch=buttons_batch)
money_sprite = Sprite(buttons[4], x=248, y=250, batch=buttons_batch)
selected_sprite = Sprite(buttons[5], x=-248, y=-250, batch=buttons_batch)


def on_hint(self, x, y):
    if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
        return True
    else:
        return False


def on_mouse_press(x, y, button, modifiers):
    if on_hint(status_sprite, x, y):
        selected_sprite.x = status_sprite.x
        selected_sprite.y = status_sprite.y
        status_name.status_name_draw()
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


def draw_sprites():
    pet.sprite.draw()
    buttons_batch.draw()
    status_name.sprite.draw()
    status_name.text_draw()


def update():
    pyglet.clock.schedule_interval(pet.update, interval=0.6)