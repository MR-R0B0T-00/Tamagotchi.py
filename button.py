import pyglet


class Button(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.press = False
