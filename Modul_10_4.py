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
        a = randint(3,10)
        sleep(a)

class Cafe:
    def __init__(self, *tabl_):
        self.tables = []
        for i in tabl_:
            self.tables.append(i)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                else:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')




#
# def run(self):
#         print('Лодка вышла в море...', flush=True)
#         for fisher in self.fishers:
#             fisher.start()
#         while True:
#             try:
#                 # Этот метод у очереди - атомарный и блокирующий,
#                 # Поток приостанавливается, пока нет элементов в очереди
#                 fish = self.catcher.get(timeout=1)
#                 print(f'Приемщик принял {fish} и положил в садок', flush=True)
#                 self.fish_tank[fish] += 1
#             except queue.Empty:
#                 print(f'Приемщику нет рыбы в течении 1 секунды', flush=True)
#                 if not any(fisher.is_alive() for fisher in self.fishers):
#                     break
#         for fisher in self.fishers:
#             fisher.join()
#         print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)


