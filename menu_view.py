import pyglet
from pyglet.text import Label
from datetime import datetime
from load_resources import layout_img, foods_img


def draw_text(list_text):
    for text in list_text:
        text.visible = True


def clear_text(list_text):
    for text in list_text:
        text.visible = False


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
        self.food = False
        self.salad = pyglet.sprite.Sprite(foods_img[0], x=110, y=110, batch=self.text_batch)
        self.meat = pyglet.sprite.Sprite(foods_img[1], x=110, y=110, batch=self.text_batch)
        self.cake = pyglet.sprite.Sprite(foods_img[2], x=110, y=110, batch=self.text_batch)
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
        self.list_text = [self.date, self.time, self.name, self.health, self.hungry,
                          self.knowledge, self.money, self.age, self.salad, self.meat, self.cake]
        clear_text(self.list_text)

    def update(self, dt):
        if self.active:
            self.visible = True
        if not self.active:
            self.visible = False
        self.draw_info()
        self.draw_status()
        self.draw_food()

    def draw_info(self):
        if self.info:
            self.date.text = f'Date: {datetime.now().strftime("%d/%m/%Y")}'
            self.time.text = f'Time: {datetime.now().strftime("%H:%M:%S")}'
            draw_text([self.date, self.time])
        if not self.info:
            clear_text([self.date, self.time])

    def draw_status(self):
        if self.status:
            self.age.text = f'Age: {self.pet.age}'
            self.health.text = f'Health: {self.pet.health}%'
            self.hungry.text = f'Hungry: {self.pet.hungry}%'
            self.knowledge.text = f'Knowledge: {self.pet.knowledge}%'
            self.money.text = f'Money: {self.pet.money} rub'
            draw_text([self.name, self.health, self.hungry, self.knowledge,
                       self.money, self.age])
        if not self.status:
            clear_text([self.name, self.health, self.hungry, self.knowledge,
                       self.money, self.age])

    def draw_food(self):
        if self.food:
            self.meat.visible = True
        if not self.food:
            self.meat.visible = False

    def draw_toilet(self):
        pass

    def draw_game(self):
        pass

    def draw_shop(self):
        pass

    def draw_study(self):
        pass

    def draw_work(self):
        pass

    def draw_hospital(self):
        pass

    def draw_email(self):
        pass
