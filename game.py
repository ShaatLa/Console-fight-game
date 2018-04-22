import random
from time import sleep

import keyboard


class Person:
    def __init__(self, name, health, strength, armor, damage):
        self.name = name
        self.health = health
        self.strength = strength
        self.armor = armor
        self.damage = damage

    def hit(self):
        hit = int(random.randint(self.damage, self.damage + self.strength))
        return hit


class User(Person):
    def choose_attack_side(self):
        side = None
        print('Выберите сторону для атаки.')
        while side != 'left' or side != 'right':
            side = keyboard.read_shortcut()
            if side == 'left':
                print('Вы атакуете налево и... ', end='')
                sleep(0.2)
                return 'left'
            elif side == 'right':
                print('Вы атакуете направо и... ', end='')
                sleep(0.2)
                return 'right'
            else:
                print('Выберите сторону клавишами стрелочек...')

    def choose_dodge_side(self):
        side = ''
        print('Выберите сторону для уклонения.')
        while side != 'left' or side != 'right':
            side = keyboard.read_shortcut()
            if side == 'left':
                print('Вы отпрыгнули влево и... ', end='')
                sleep(0.2)
                return 'left'
            elif side == 'right':
                print('Вы отпрыгнули вправо и... ', end='')
                sleep(0.2)
                return 'right'
            else:
                print('Выберите сторону клавишами стрелочек...')


class Mob(Person):
    def mob_choice(self):
        return random.choice(['left', 'right'])


class Game:
    def loading(self):
        for i in range(1, 102, 3):
            print(f'\rЗагрузка игры: {1 * i}%', end='')
            sleep(0.01)
        print('\n\nДобро пожаловать в подземелье! Вы - герой, который сражается с монстром!')
        print('Уклоняйтесь от него с помощью клавиш стрелочек влево и вправо.')
        print('Угадывайте в какую сторону будет атаковать и отпрыгивать монстр!\n')
        sleep(6)
        print('Удачи!\n')
        sleep(2)
        print('Бой начинается!\n')
        sleep(0.5)

    def good_bye(self):
        print('\nИгра закончена, до новых встреч!')
        for i in range(1, 10):
            print(f'\rКоносоль закроется автоматически через: {10 - i}', end=' ')
            sleep(1)
        exit()

    def gameplay(self, user, mob):
        while True:
            if user.health > 0 and mob.health > 0:
                print(f'{mob.name} нападает!', end=' ')
                if mob.mob_choice() == user.choose_dodge_side():
                    hit = mob.hit()
                    user.health = user.health - hit
                    print(f'{mob.name} наносит {hit} урона. Здоровье {user.name}: {user.health}\n')
                    sleep(1)
                else:
                    print('Вы уклонились от удара монстра!\n')
                    sleep(0.5)
            elif mob.health <= 0:
                winner = user.name
                loser = mob.name
                break
            if mob.health > 0 and user.health > 0:
                print(f'Вы атакуете!', end=' ')
                if mob.mob_choice() == user.choose_attack_side():
                    hit = user.hit()
                    mob.health = mob.health - hit
                    print(f'Вы наносите {hit} урона. Здоровье {mob.name}а: {mob.health}\n')
                    sleep(1)
                else:
                    print(f'{mob.name} уклонился от вашего удара...\n')
                    sleep(0.5)
            elif user.health <= 0:
                winner = mob.name
                loser = user.name
                break
            else:
                print('Ошибка...')
        print(f'{loser} проиграл. {winner} победил.')


user = User(input('Введите имя игрока: '),
            100,
            int(int(input('Введите ваш вес: ')) / 1.65),
            random.uniform(1, 2),
            int(int(input('Введите ваш возраст: ')) / 1.65))

mob = Mob(random.choice(['Вурдалак', 'Оборотень', 'Зомби', 'Чупакабра', 'Киборг']),
          100,
          random.randint(20, 31),
          random.uniform(1, 2),
          random.randint(20, 31))

Game.loading(Game)
Game.gameplay(Game, user, mob)
Game.good_bye(Game)
