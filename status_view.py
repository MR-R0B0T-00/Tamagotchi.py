import pyglet

pyglet.font.add_file('fonts/pixeltiny.ttf')


class Status:
    def __init__(self, pet):
        self.img = pyglet.image.load('img/sprites/menu/layout_info.png')
        self.sprite = pyglet.sprite.Sprite(self.img, x=-500, y=40)
        self.pet = pet
        self.font = pyglet.font.load('PixelTiny')
        self.name = pyglet.text.Label(f'Name: {self.pet.name}', x=-500, y=190,
                                      font_name='PixelTiny', font_size=40)
        self.age = pyglet.text.Label(f'Age: {self.pet.age}', x=-500, y=160,
                                     font_name='PixelTiny', font_size=40)
        self.health = pyglet.text.Label(f'Health: {self.pet.health}%', x=-500, y=130,
                                        font_name='PixelTiny', font_size=40)
        self.hungry = pyglet.text.Label(f'Hungry: {self.pet.hungry}%', x=-500, y=100,
                                        font_name='PixelTiny', font_size=40)
        self.sleep = pyglet.text.Label(f'Sleep: {self.pet.sleep}%', x=-500, y=70,
                                       font_name='PixelTiny', font_size=40)

    def status_name_draw(self):
        self.sprite.x = 8
        self.name.x = 18
        self.age.x = 18
        self.health.x = 18
        self.hungry.x = 18
        self.sleep.x = 18

    def text_draw(self):
        self.name.draw()
        self.age.draw()
        self.health.draw()
        self.hungry.draw()
        self.sleep.draw()
