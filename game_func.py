import pyglet
import animals
import load_resources
from status_view import Status
from button import Button

buttons_batch = pyglet.graphics.Batch()
status_batch = pyglet.graphics.Batch()
soft_bars = pyglet.graphics.Batch()

pet = animals.Dog('Bob')
status = Status(pet, batch=status_batch)

status_button = Button(load_resources.status_img, x=30, y=275, batch=buttons_batch)
food_button = Button(load_resources.food_img, x=status_button.x + 60, y=275, batch=buttons_batch)
health_button = Button(load_resources.health_img, x=food_button.x + 60, y=275, batch=buttons_batch)
enjoy_button = Button(load_resources.games_img, x=health_button.x + 60, y=275, batch=buttons_batch)
money_button = Button(load_resources.money_img, x=enjoy_button.x + 60, y=275, batch=buttons_batch)


soft_bar_up = pyglet.sprite.Sprite(load_resources.soft_bar, x=150, y=285, batch=soft_bars)
soft_bar_down = pyglet.sprite.Sprite(load_resources.soft_bar, x=150, y=15, batch=soft_bars)
soft_bar_down.rotation = 180


def draw_sprites():
    pet.sprite.draw()
    soft_bars.draw()
    buttons_batch.draw()


def update(dt):
    pet.update(dt)
