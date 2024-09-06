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
    def __init__(self, *tables):
        for i in tables:
            self.table = i
        self.q = queue.Queue()

    def guest_arrival(self, *guests):




