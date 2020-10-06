from crewmate import Crewmate
from task import Task
import random

class Impostor(Crewmate):
    def __init__(self, name):
        '''How is this different from the character class I hate myself'''
        self.name = name
        self.tasks = list()
        self.location = 'Cafeteria'
        self.is_alive = True

        for x in Task.sabotage_tasks:
            t = Task(x, Task.sabotage_tasks[x])
            self.tasks.append(t)

    def sabotage(self):
        choice = random.choice(self.tasks)
        return choice

    def murder(self, name):
        pass