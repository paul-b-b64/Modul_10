from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        a = randint(3, 10)
        sleep(a)


class Cafe:
    def __init__(self, *tabl_):
        self.tables = []
        for i in tabl_:
            self.tables.append(i)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        self.guests = []
        for guest in guests:
            if all(table.guest != None for table in self.tables):
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
            else:
                for table in self.tables:
                    if table.guest == None:
                        table.guest = guest
                        guest.start()
                        guest.join()
                        print(f'{guest.name} сел(-а) за стол номер {table.number}')
                        break

    def discuss_guests(self):
        while not self.queue.empty() and not all(table.guest == None for table in self.tables):
            for table in self.tables:
                if table.guest == None and not self.queue.empty():
                    guest = self.queue.get()
                    table.guest = guest
                    guest.start()
                    guest.join()
                    print(f'{table.guest.name} вышел из очереди и сел за стол номер {table.number}')
                elif table.guest != None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал и ушел')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    break


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
