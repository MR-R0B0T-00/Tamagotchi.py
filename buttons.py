from pyglet.sprite import Sprite
from pyglet.text import Label
from datetime import datetime


class StatusButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(StatusButton, self).__init__(*args, **kwargs)
        self.x, self.y = 30, 205

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class FoodButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(FoodButton, self).__init__(*args, **kwargs)
        self.x, self.y = 70, 205

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class ToiletButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(ToiletButton, self).__init__(*args, **kwargs)
        self.x, self.y = 110, 205

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class GameButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(GameButton, self).__init__(*args, **kwargs)
        self.x, self.y = 150, 205

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class ShopButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(ShopButton, self).__init__(*args, **kwargs)
        self.x, self.y = 190, 205

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class StudyButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(StudyButton, self).__init__(*args, **kwargs)
        self.x, self.y = 30, 15

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class WorkButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(WorkButton, self).__init__(*args, **kwargs)
        self.x, self.y = 70, 15

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class AidsButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(AidsButton, self).__init__(*args, **kwargs)
        self.x, self.y = 110, 15

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class MailButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(MailButton, self).__init__(*args, **kwargs)
        self.x, self.y = 150, 15

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')


class InfoButton(Sprite):
    def __init__(self, *args, **kwargs):
        super(InfoButton, self).__init__(*args, **kwargs)
        self.x, self.y = 190, 15

    def update(self, dt):
        print(dt)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:
            print('Status')
    #     self.date = Label('', 'PixelTiny', 30,
    #                       batch=self.batch, x=110, y=130, anchor_x='center', anchor_y='center')
    #     self.time = Label('', 'PixelTiny', 30,
    #                       batch=self.batch, x=110, y=110, anchor_x='center', anchor_y='center')
    #     self.date.visible, self.time.visible = False, False
    #
    # def update(self, dt):
    #     pass
    #     # if self.on_mouse_release:
    #     #     print('time')
    #     #     self.date.text = f'Date: {datetime.now().strftime("%d/%m/%Y")}'
    #     #     self.time.text = f'Time: {datetime.now().strftime("%H:%M:%S")}'
    #     # if not self.active_layout:
    #     #     self.date.visible, self.time.visible = False, False
