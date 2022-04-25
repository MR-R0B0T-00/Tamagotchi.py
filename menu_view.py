import pyglet
from load_resources import layout_img


class Menu(pyglet.sprite.Sprite):
    def __init__(self, pet, *args, **kwargs):
        super(Menu, self).__init__(layout_img, *args, **kwargs)
        self.pet = pet
        self.x, self.y = -200, 110
        self.active = False
        self.name = pyglet.text.Label(f'Name: {self.pet.name}', x=-500, y=190,
                                      font_name='PixelTiny', font_size=40)
        self.age = pyglet.text.Label(f'Age: {self.pet.age}', x=-500, y=160,
                                     font_name='PixelTiny', font_size=40)
        self.health = pyglet.text.Label(f'Health: {self.pet.health}%', x=-500, y=130,
                                        font_name='PixelTiny', font_size=40)
        self.hungry = pyglet.text.Label(f'Hungry: {self.pet.hungry}%', x=-500, y=100,
                                        font_name='PixelTiny', font_size=40)

    def update(self, dt):
        if self.active:
            self.x = 110
        if not self.active:
            self.x = -500
