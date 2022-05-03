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
        self.date = Label('', 'PixelTiny', 30,
                          batch=self.text_batch, x=110, y=130, anchor_x='center', anchor_y='center')
        self.time = Label('', 'PixelTiny', 30,
                          batch=self.text_batch, x=110, y=110, anchor_x='center', anchor_y='center')
        self.date.visible, self.time.visible = False, False

    def update(self, dt):
        if self.active:
            self.visible = True
        if not self.active:
            self.visible = False
        self.draw_info()

    def draw_info(self):
        if self.info:
            self.date.text = f'Date: {datetime.now().strftime("%d/%m/%Y")}'
            self.time.text = f'Time: {datetime.now().strftime("%H:%M:%S")}'
            self.date.visible, self.time.visible = True, True
        if not self.info:
            self.date.visible, self.time.visible = False, False

    # def draw_status(self):
    #     if self.status and self.active:
    #         self.name = Label(f'Name: {self.pet.name}', x=20, y=158,
    #                           font_name='PixelTiny', font_size=30,
    #                           batch=self.text_batch)
    #         self.age = Label(f'Age: {self.pet.age}', x=20, y=137,
    #                          font_name='PixelTiny', font_size=30,
    #                          batch=self.text_batch)
    #         self.health = Label(f'Health: {self.pet.health}%', x=20, y=116,
    #                             font_name='PixelTiny', font_size=30,
    #                             batch=self.text_batch)
    #         self.hungry = Label(f'Hungry: {self.pet.hungry}%', x=20, y=95,
    #                             font_name='PixelTiny', font_size=30,
    #                             batch=self.text_batch)
    #         self.knowledge = Label(f'Knowledge: {self.pet.knowledge}%', x=20, y=74,
    #                                font_name='PixelTiny', font_size=30,
    #                                batch=self.text_batch)
    #         self.money = Label(f'Money: {self.pet.money} rub', x=20, y=53,
    #                            font_name='PixelTiny', font_size=30,
    #                            batch=self.text_batch)
    #     if not self.status:
    #         self.text_batch.draw()
