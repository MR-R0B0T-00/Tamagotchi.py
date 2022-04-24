import pyglet
import animals
import load_resources
from status_view import Status
from pyglet.sprite import Sprite

main_batch = pyglet.graphics.Batch()
status_batch = pyglet.graphics.Batch()

pet = animals.Dog('Bob', batch=main_batch)
status = Status(pet, batch=status_batch)

soft_bar_up = pyglet.sprite.Sprite(load_resources.soft_bar, x=110, y=205, batch=main_batch)
soft_bar_down = pyglet.sprite.Sprite(load_resources.soft_bar, x=110, y=15, batch=main_batch)
soft_bar_down.rotation = 180

status_button = Sprite(load_resources.status_img, x=30, y=soft_bar_up.y, batch=main_batch)
food_button = Sprite(load_resources.food_img, x=70, y=soft_bar_up.y, batch=main_batch)
toilet_button = Sprite(load_resources.toilet_img, x=110, y=soft_bar_up.y, batch=main_batch)
game_button = Sprite(load_resources.games_img, x=150, y=soft_bar_up.y, batch=main_batch)
shop_button = Sprite(load_resources.shop_img, x=190, y=soft_bar_up.y, batch=main_batch)

study_button = Sprite(load_resources.study_img, x=30, y=soft_bar_down.y, batch=main_batch)
work_button = Sprite(load_resources.work_img, x=70, y=soft_bar_down.y, batch=main_batch)
aids_button = Sprite(load_resources.aids_img, x=110, y=soft_bar_down.y, batch=main_batch)
mail_button = Sprite(load_resources.mail_img, x=150, y=soft_bar_down.y, batch=main_batch)
info_button = Sprite(load_resources.info_img, x=190, y=soft_bar_down.y, batch=main_batch)


def push_button(btn, x, y):
    if btn.x - 10 <= x <= btn.x + 10 and btn.y - 10 <= y <= btn.y + 10:
        return True


def on_mouse_release(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        if push_button(status_button, x, y):
            status.status_name_draw()
        if push_button(food_button, x, y):
            print('food')
        if push_button(toilet_button, x, y):
            print('toilet')
        if push_button(game_button, x, y):
            print('games')
        if push_button(shop_button, x, y):
            print('shop')
        if push_button(study_button, x, y):
            print('study')
        if push_button(work_button, x, y):
            print('work')
        if push_button(aids_button, x, y):
            print('aids')
        if push_button(mail_button, x, y):
            print('mail')
        if push_button(info_button, x, y):
            print('info')

