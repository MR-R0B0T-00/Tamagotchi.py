import pyglet
import animals
import load_resources
from pyglet.sprite import Sprite
import buttons

main_batch = pyglet.graphics.Batch()

pet = animals.Dog('Bob', batch=main_batch)
layout = Sprite(load_resources.layout_img, x=110, y=110, batch=main_batch)
layout.visible = False

soft_bar_up = Sprite(load_resources.soft_bar, x=110, y=205, batch=main_batch)
soft_bar_down = Sprite(load_resources.soft_bar, x=110, y=15, batch=main_batch)
soft_bar_down.rotation = 180

status_button = buttons.StatusButton(pet=pet, img=load_resources.status_img, batch=main_batch)
food_button = buttons.FoodButton(load_resources.food_img, batch=main_batch)
toilet_button = buttons.ToiletButton(load_resources.toilet_img, batch=main_batch)
game_button = buttons.GameButton(load_resources.games_img, batch=main_batch)
shop_button = buttons.ShopButton(load_resources.shop_img, batch=main_batch)

study_button = buttons.StudyButton(load_resources.study_img, batch=main_batch)
work_button = buttons.WorkButton(load_resources.work_img, batch=main_batch)
aids_button = buttons.AidsButton(load_resources.aids_img, batch=main_batch)
mail_button = buttons.MailButton(load_resources.mail_img, batch=main_batch)
info_button = buttons.InfoButton(load_resources.info_img, batch=main_batch)


def push_close(x, y):
    if 185 <= x <= 210 and 160 <= y <= 175:
        return True


def on_mouse_release(x, y, button, modifiers):
    for button in [status_button, food_button, toilet_button, game_button, shop_button, study_button,
                   work_button, aids_button, mail_button, info_button]:
        if button.active and push_close(x, y):
            button.active = False
            layout.visible = False


events_mouse = [status_button.on_mouse_release, food_button.on_mouse_release, toilet_button.on_mouse_release,
                game_button.on_mouse_release, shop_button.on_mouse_release, study_button.on_mouse_release,
                work_button.on_mouse_release, aids_button.on_mouse_release, mail_button.on_mouse_release,
                info_button.on_mouse_release, on_mouse_release]


def update_game(dt):
    pet.update(dt)
    for button in [status_button, food_button, toilet_button, game_button, shop_button, study_button,
                   work_button, aids_button, mail_button, info_button]:
        button.update(dt)
        if button.active:
            layout.visible = True

# def on_mouse_release(x, y, button, modifiers):
#     if button == pyglet.window.mouse.LEFT:
#         if push_button(status_button, x, y):
#             if not menu.active:
#                 menu.active = True
#                 menu.status = True
#         if push_button(food_button, x, y):
#             if not menu.active:
#                 menu.active = True
#                 menu.food = True
#         if push_button(toilet_button, x, y):
#             if not menu.active:
#                 menu.active = True
#         if push_button(game_button, x, y):
#             if not menu.active:
#                 menu.active = True
#         if push_button(shop_button, x, y):
#             if not menu.active:
#                 menu.active = True
#         if push_button(study_button, x, y):
#             if not menu.active:
#                 menu.active = True
#         if push_button(work_button, x, y):
#             if not menu.active:
#                 menu.active = True
#         if push_button(aids_button, x, y):
#             if not menu.active:
#                 menu.active = True
#         if push_button(mail_button, x, y):
#             if not menu.active:
#                 menu.active = True
#         if push_button(info_button, x, y):
#             if not menu.active:
#                 menu.active = True
#                 menu.info = True
#         if menu.active:
#             if push_close(x, y):
#                 menu.active = False
#                 menu.status = False
#                 menu.info = False
#                 menu.food = False
