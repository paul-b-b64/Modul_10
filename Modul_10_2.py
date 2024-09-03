from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        self.enemy = 100
        self.day = 0
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            self.enemy -= self.power
            self.day += 1
            sleep(1)
            print(f'{self.name} сражается {self.day} дня(дней), осталось {self.enemy} воинов')
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
