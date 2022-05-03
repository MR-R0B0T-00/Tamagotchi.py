import pyglet
from pyglet.text import Label
from datetime import datetime
from load_resources import layout_img


class Menu(pyglet.sprite.Sprite):
    def __init__(self, pet, *args, **kwargs):
        super(Menu, self).__init__(layout_img, *args, **kwargs)
        self.x, self.y = 110, 110
        self.visible = False
        self.pet = pet
        self.text_batch = pyglet.graphics.Batch()
        self.active = False
        self.status = False
        self.info = False
        self.name = Label(self.pet.name, 'PixelTiny', 30,
                          batch=self.text_batch, x=110, y=175, anchor_x='center', anchor_y='center')
        self.age = Label('', 'PixelTiny', 30,
                         batch=self.text_batch, x=20, y=155, anchor_y='center')
        self.health = Label('', x=20, y=135, anchor_y='center',
                            font_name='PixelTiny', font_size=30, batch=self.text_batch)
        self.hungry = Label('', x=20, y=115, anchor_y='center',
                            font_name='PixelTiny', font_size=30, batch=self.text_batch)
        self.knowledge = Label('', x=20, y=95, anchor_y='center',
                               font_name='PixelTiny', font_size=30, batch=self.text_batch)
        self.money = Label('', x=20, y=75, anchor_y='center',
                           font_name='PixelTiny', font_size=30, batch=self.text_batch)
        self.date = Label('', 'PixelTiny', 30,
                          batch=self.text_batch, x=110, y=130, anchor_x='center', anchor_y='center')
        self.time = Label('', 'PixelTiny', 30,
                          batch=self.text_batch, x=110, y=110, anchor_x='center', anchor_y='center')
        self.date.visible, self.time.visible = False, False
        self.name.visible, self.health.visible, self.hungry.visible = False, False, False
        self.knowledge.visible, self.money.visible, self.age.visible = False, False, False

    def update(self, dt):
        if self.active:
            self.visible = True
        if not self.active:
            self.visible = False
        self.draw_info()
        self.draw_status()

    def draw_info(self):
        if self.info:
            self.date.text = f'Date: {datetime.now().strftime("%d/%m/%Y")}'
            self.time.text = f'Time: {datetime.now().strftime("%H:%M:%S")}'
            self.date.visible, self.time.visible = True, True
        if not self.info:
            self.date.visible, self.time.visible = False, False

    def draw_status(self):
        if self.status:
            self.age.text = f'Age: {self.pet.age}'
            self.health.text = f'Health: {self.pet.health}%'
            self.hungry.text = f'Hungry: {self.pet.hungry}%'
            self.knowledge.text = f'Knowledge: {self.pet.knowledge}%'
            self.money.text = f'Money: {self.pet.money} rub'
            self.name.visible, self.health.visible, self.hungry.visible = True, True, True
            self.knowledge.visible, self.money.visible, self.age.visible = True, True, True
        if not self.status:
            self.name.visible, self.health.visible, self.hungry.visible = False, False, False
            self.knowledge.visible, self.money.visible, self.age.visible = False, False, False
