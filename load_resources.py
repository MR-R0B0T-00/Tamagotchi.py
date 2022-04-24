import pyglet

pyglet.resource.path = ['img/sprites/menu/', 'img/sprites/animals/', 'img/backgrounds/']
pyglet.font.add_file('fonts/pixeltiny.ttf')
font = pyglet.font.load('PixelTiny')
pyglet.resource.reindex()

background = pyglet.resource.image('bg_main.png')
soft_bar = pyglet.resource.image('softbar.png')
layout_img = pyglet.resource.image('layout_info.png')
status_img = pyglet.resource.image('gui_menu.png').get_region(0, 0, 20, 20)
food_img = pyglet.resource.image('gui_menu.png').get_region(20, 0, 20, 20)
toilet_img = pyglet.resource.image('gui_menu.png').get_region(40, 0, 20, 20)
games_img = pyglet.resource.image('gui_menu.png').get_region(60, 0, 20, 20)
shop_img = pyglet.resource.image('gui_menu.png').get_region(80, 0, 20, 20)
study_img = pyglet.resource.image('gui_menu.png').get_region(100, 0, 20, 20)
work_img = pyglet.resource.image('gui_menu.png').get_region(120, 0, 20, 20)
aids_img = pyglet.resource.image('gui_menu.png').get_region(140, 0, 20, 20)
mail_img = pyglet.resource.image('gui_menu.png').get_region(160, 0, 20, 20)
info_img = pyglet.resource.image('gui_menu.png').get_region(180, 0, 20, 20)
dog_img = [pyglet.resource.image('dog.png').get_region(0, 0, 45, 75),
           pyglet.resource.image('dog.png').get_region(45, 0, 45, 75),
           pyglet.resource.image('dog.png').get_region(90, 0, 45, 75)]


def center_img(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


for img in [status_img, layout_img, soft_bar, food_img, toilet_img, games_img, shop_img, study_img,
            aids_img, mail_img, info_img, background, work_img]:
    center_img(img)

for dog in dog_img:
    center_img(dog)
