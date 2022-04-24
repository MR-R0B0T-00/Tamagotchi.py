import pyglet
from load_resources import layout_img


class Status(pyglet.sprite.Sprite):
    def __init__(self, pet, *args, **kwargs):
        super(Status, self).__init__(layout_img, *args, **kwargs)
        self.pet = pet
        self.font = pyglet.font.load('PixelTiny')
        self.name = pyglet.text.Label(f'Name: {self.pet.name}', x=-500, y=190,
                                      font_name='PixelTiny', font_size=40, batch=self.batch)
        self.age = pyglet.text.Label(f'Age: {self.pet.age}', x=-500, y=160,
                                     font_name='PixelTiny', font_size=40, batch=self.batch)
        self.health = pyglet.text.Label(f'Health: {self.pet.health}%', x=-500, y=130,
                                        font_name='PixelTiny', font_size=40, batch=self.batch)
        self.hungry = pyglet.text.Label(f'Hungry: {self.pet.hungry}%', x=-500, y=100,
                                        font_name='PixelTiny', font_size=40, batch=self.batch)
        self.sleep = pyglet.text.Label(f'Sleep: {self.pet.sleep}%', x=-500, y=70,
                                       font_name='PixelTiny', font_size=40, batch=self.batch)

    def status_name_draw(self):
        self.sprite.x = 8
        self.name.x = 18
        self.age.x = 18
        self.health.x = 18
        self.hungry.x = 18
        self.sleep.x = 18

    # def text_draw(self):
    #     self.name.draw()
    #     self.age.draw()
    #     self.health.draw()
    #     self.hungry.draw()
    #     self.sleep.draw()
