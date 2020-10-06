from task import Task
import random

class Crewmate:
    game_map = ['Dropship', 'Upper Engine', 'Lower Engine', 'Reactor', 'Navigation', 'Shields', 'Weapons', 'Comms', 'Storage', 'MedBay', 'Electrical', 'Oxygen', 'Security']

    def __init__(self, name):
        '''How is this different from the character class I hate myself'''
        self.name = name
        self.tasks = list()
        self.location = 'Cafeteria'
        self.free_to_move = True
        self.is_alive = True

    def add_task(self, name, location):
        #print(name)
        #print(location)
        t = Task(name, location)
        self.tasks.append(t)
        return t

    def roam(self):
        place = random.choice(self.game_map)
        self.location = place

if __name__ == "__main__":
    testboi = Crewmate('red')
    testboi.add_task('Clean O2 Filter', 'Oxygen')
    print(testboi.tasks[0].name)

