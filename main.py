import schedule


class Pet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.hungry = 30
        self.fun = 70
        self.sleep = 100

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


def run_game():
    pet = Pet(input('Введите имя питомца: '))
    schedule.every(5).seconds.do(pet.not_eat)
    schedule.every(2).minutes.do(pet.not_sleep)

    def update():
        schedule.run_pending()

    while True:
        cmd = input('Введите команду: ')
        if cmd == 'status':
            pet.status()
        elif cmd == 'feed':
            pet.eat()
        elif cmd == 'to heal':
            pet.to_heal()
        elif cmd == 'entertain':
            pet.funny()
        update()


if __name__ == '__main__':
    run_game()
