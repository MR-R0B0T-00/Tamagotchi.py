import pyglet
import load_resources


class Animal(pyglet.sprite.Sprite):
    def __init__(self, name, *args, **kwargs):
        super(Animal, self).__init__(*args, **kwargs)
        self.name = name
        self.age = 0
        self.health = 100
        self.hungry = 30
        self.learning = 10
        self.happy = 50
        self.toilet = 70
        self.money = 0
        
    def update(self, dt):
        pass

    # def eat(self):
    #     if self.hungry > 0:
    #         self.hungry -= 10
    #         if self.hungry < 0:
    #             self.hungry = 0
    #     print('Голод --')
    #
    # def funny(self):
    #     if self.fun < 100:
    #         self.fun += 10
    #         if self.fun > 100:
    #             self.fun = 100
    #     print('Веселье ++')
    #
    # def birthday(self):
    #     self.age += 1
    #     print('Возраст ++')
    #
    # def to_heal(self):
    #     if self.health < 100:
    #         self.health += 10
    #         if self.health > 100:
    #             self.health = 100
    #     print('Здоровье ++')
    #
    # def to_sleep(self):
    #     if self.sleep < 100:
    #         self.sleep += 10
    #         if self.sleep > 100:
    #             self.sleep = 100
    #     print('Сон ++')
    #
    # def not_eat(self):
    #     self.hungry += 10
    #     if self.hungry > 100:
    #         self.hungry = 100
    #     print('Голод ++')


class Dog(Animal):
    def __init__(self, name, *args, **kwargs):
        self.animation = pyglet.image.Animation.from_image_sequence(load_resources.dog_img, duration=1 / 3, loop=True)
        super().__init__(name, self.animation, *args, **kwargs)
        self.x, self.y = 150, 75
        self.right_move = True
        self.left_move = False

    def update(self, dt):  # dt - Это интервал, без него функция не работает
        super(Dog, self).update(dt)
        if self.right_move and self.x <= 165:
            self.x += 20
        else:
            self.right_move = False
            self.left_move = True
        if self.left_move and self.x >= 60:
            self.x -= 20
        else:
            self.right_move = True
            self.left_move = False
