import pyglet


class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.hungry = 30
        self.images = [pyglet.resource.image('img/sprites/animals/dog_1.png'),
                       pyglet.resource.image('img/sprites/animals/dog_2.png'),
                       pyglet.resource.image('img/sprites/animals/dog_3.png')]
        self.animation = pyglet.image.Animation.from_image_sequence(self.images, duration=0.6, loop=True)
        self.sprite = pyglet.sprite.Sprite(self.animation, x=150 - 22, y=150 - 85)
        self.right_move = True
        self.left_move = False

    def update(self, dt):  # dt - Это интервал, без него функция не работает
        if self.right_move:
            self.sprite.x -= 20
            if self.sprite.x <= 0:
                self.right_move = False
                self.left_move = True
        if self.left_move:
            self.sprite.x += 20
            if self.sprite.x >= 230:
                self.right_move = True
                self.left_move = False

    def status(self):
        print(f'== {self.name} ==')
        print(f'** Возраст: {self.age}')
        print(f'** Здоровье: {self.health}%')
        print(f'** Голод: {self.hungry}%')
        print(f'** Настроение: {self.fun}%')
        print(f'** Сон: {self.sleep}%')

    def eat(self):
        if self.hungry > 0:
            self.hungry -= 10
            if self.hungry < 0:
                self.hungry = 0
        print('Голод --')

    def funny(self):
        if self.fun < 100:
            self.fun += 10
            if self.fun > 100:
                self.fun = 100
        print('Веселье ++')

    def birthday(self):
        self.age += 1
        print('Возраст ++')

    def to_heal(self):
        if self.health < 100:
            self.health += 10
            if self.health > 100:
                self.health = 100
        print('Здоровье ++')

    def to_sleep(self):
        if self.sleep < 100:
            self.sleep += 10
            if self.sleep > 100:
                self.sleep = 100
        print('Сон ++')

    def not_eat(self):
        self.hungry += 10
        if self.hungry > 100:
            self.hungry = 100
        print('Голод ++')

    def not_sleep(self):
        self.sleep -= 10
        if self.sleep < 0:
            self.sleep = 0
        print('Сон --')
