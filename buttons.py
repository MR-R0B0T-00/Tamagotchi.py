from pyglet.sprite import Sprite
from pyglet.text import Label
import pyglet
from datetime import datetime

text_batch = pyglet.graphics.Batch()


def draw_text(list_text):
    for text in list_text:
        text.visible = True


def clear_text(list_text):
    for text in list_text:
        text.visible = False


class StatusButton(Sprite):
    def __init__(self, pet, *args, **kwargs):
        super(StatusButton, self).__init__(*args, **kwargs)
        self.pet = pet
        self.x, self.y = 30, 205
        self.active = False
        self.name = Label(self.pet.name, 'PixelTiny', 30,
                          batch=text_batch, x=110, y=175, anchor_x='center', anchor_y='center')
        self.age = Label('', 'PixelTiny', 30,
                         batch=text_batch, x=20, y=155, anchor_y='center')
        self.health = Label('', x=20, y=135, anchor_y='center',
                            font_name='PixelTiny', font_size=30, batch=text_batch)
        self.hungry = Label('', x=20, y=115, anchor_y='center',
                            font_name='PixelTiny', font_size=30, batch=text_batch)
        self.knowledge = Label('', x=20, y=95, anchor_y='center',
                               font_name='PixelTiny', font_size=30, batch=text_batch)
        self.money = Label('', x=20, y=75, anchor_y='center',
                           font_name='PixelTiny', font_size=30, batch=text_batch)
        self.list_text = [self.name, self.health, self.hungry, self.knowledge, self.money, self.age]
        clear_text(self.list_text)

    def update(self, dt):
        if self.active:
            self.age.text = f'Age: {self.pet.age}'
            self.health.text = f'Health: {self.pet.health}%'
            draw_text(self.list_text)
        else:
            clear_text(self.list_text)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            self.active = True


class FoodButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(FoodButton, self).__init__(*args, **kwargs)
        self.x, self.y = 70, 205
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class ToiletButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(ToiletButton, self).__init__(*args, **kwargs)
        self.x, self.y = 110, 205
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class GameButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(GameButton, self).__init__(*args, **kwargs)
        self.x, self.y = 150, 205
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class ShopButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(ShopButton, self).__init__(*args, **kwargs)
        self.x, self.y = 190, 205
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class StudyButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(StudyButton, self).__init__(*args, **kwargs)
        self.x, self.y = 30, 15
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class WorkButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(WorkButton, self).__init__(*args, **kwargs)
        self.x, self.y = 70, 15
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class AidsButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(AidsButton, self).__init__(*args, **kwargs)
        self.x, self.y = 110, 15
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class MailButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(MailButton, self).__init__(*args, **kwargs)
        self.x, self.y = 150, 15
        self.active = False

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class InfoButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(InfoButton, self).__init__(*args, **kwargs)
        self.x, self.y = 190, 15
        self.active = False
        self.date = Label('', 'PixelTiny', 30,
                          batch=text_batch, x=110, y=130, anchor_x='center', anchor_y='center')
        self.time = Label('', 'PixelTiny', 30,
                          batch=text_batch, x=110, y=110, anchor_x='center', anchor_y='center')
        self.list_text = [self.date, self.time]
        clear_text(self.list_text)

    def update(self, dt):
        if self.active:
            draw_text(self.list_text)
            self.date.text = f'Date: {datetime.now().strftime("%d/%m/%Y")}'
            self.time.text = f'Time: {datetime.now().strftime("%H:%M:%S")}'
        else:
            clear_text(self.list_text)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            self.active = True
