import pyglet
from pyglet.text import Label
from datetime import datetime
from load_resources import layout_img, foods_img


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

            draw_text([self.date, self.time])
        if not self.info:
            clear_text([self.date, self.time])

    def draw_status(self):
        if self.status:
            self.age.text =
            self.health.text =
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
