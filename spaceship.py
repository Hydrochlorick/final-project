from task import Task
from crewmate import Crewmate
from impostor import Impostor
import random

class Spaceship:
    colors = ['red', 'blue', 'green', 'pink', 'orange', 'yellow', 'black', 'white', 'purple', 'brown']

    def __init__(self):
        # Track players
        self.locations = list()
        self.living_players = list()
        self.living_crewmates = list()
        self.living_impostors = list()
        self.imp = 'null'
        self.dead_characters = list()
        self.players_left = 0

        self.tasks_remaining = list()
        self.global_tasks_left = 0

        self.meet = False
        self.gameover = False

    def kill_character(self, victim):
        for x in self.living_crewmates:
            if self.living_crewmates[x].color == victim:
                self.living_crewmates[x].is_alive = False
        for x in self.living_impostors:
            if self.living_impostors[x].color == victim:
                self.living_impostors[x].is_alive = False
        self.players_left -= 1

    # def add_crewmate(self, color, randos):
    #     crewie = Crewmate(color)
    #     self.living_crewmates.append(crewie)

    def prompt_for_players(self):
        # Idk how else to do this
        you_failed = True
        while you_failed:
            number_of_players = int(input('How many players?\n'))
            if (number_of_players < 3 or number_of_players > 10):
                print("Please enter a number between 3 and 10")
            else:
                you_failed = False
                self.living_players = random.sample(self.colors, number_of_players)
                return number_of_players
        # number_of_players -= 1
        # Generate a list of living players named by color

    def move_crewies(self):
        for x in self.living_crewmates:
            x.roam()
            if len(self.tasks_remaining) > 0:
                self.tasks_remaining.pop(random.randrange(len(self.tasks_remaining)))
        if len(self.tasks_remaining) == 0:
            print('All tasks have been completed! Crewmates win!')
            self.gameover = True

    def murder_check(self):
        # for x in self.living_impostors:
        #     impie = str(x.location)
        impie = self.imp.location
        for cc in self.living_crewmates:
            if cc.location == impie:
                cc.is_alive = False
                self.living_crewmates.remove(cc)
                print('An Impostor got someone!')
                self.players_left -= 1
                self.meet = True
                self.game_status()
                return

    def setup_game(self):
        # Decide scale of game based on user input
        self.players_left = self.prompt_for_players()
        # impostors = list()
        # if self.players_left > 6:
        #     impo1 = random.choice(self.living_players)
        #     impo2 = random.choice(self.living_players)
        #     impostors.append(impo1)
        #     impostors.append(impo2)
        # else:
        #     impostors.append(random.choice(self.living_players))

        #     print(x)
        #     if x in impostors:
        #         self.living_impostors.update(x=Impostor(x))
        #     else:
        #         self.living_crewmates.update(x=Crewmate(x))            

        # Generate two common tasks per living player
        commons = list(Task.common_tasks.keys())
        for x in self.living_players:
            playa = Crewmate(x)
            self.living_crewmates.append(playa)

            randos = list()
            somethin = random.choice(commons)
            somethinelse = random.choice(commons)
            randos.append((somethin, random.choice(Task.common_tasks[somethin])))
            randos.append((somethinelse, random.choice(Task.common_tasks[somethinelse])))
            for r in randos:
                t = Task(r[0], r[1])
                self.tasks_remaining.append(t)

            #self.players_left += 1

        # Generate unique tasks
        for x in Task.unique_tasks:
            t = Task(x, Task.unique_tasks[x])
            self.tasks_remaining.append(t)

        # Spawn players
        impo = random.choice(self.living_players)
        # Cheat
        # print(impo)
        for x in self.living_crewmates:
            boi = x.name
            if (boi == impo):
                self.living_crewmates.remove(x)
            x.roam()
        self.imp = Impostor(impo)
        self.living_impostors.append(Impostor(impo))

        # Generate a sabotage from the impostor(s)
        for x in self.living_impostors:
            t = x.sabotage()
            self.tasks_remaining.append(t)

        for t in self.tasks_remaining:
            crewie = random.choice(self.living_crewmates)
            crewie.tasks.append(t)

        print(self.living_players, self.living_impostors, self.living_crewmates)
        # print(self.global_tasks_left)
        # for x in self.unique_tasks:
        #     task = Task(x, self.unique_tasks[x])
        #     self.tasks_remaining.append(task)
        #     self.global_tasks_left += 1

    def game_status(self):
        # if (len(self.tasks_remaining == 0)):
        #     print('Game Over! Crewmates win!')
        #     self.gameover == True
        #     return
        if len(self.living_crewmates) == 0:
            print('All crewmates are dead! Impostors win!')
            self.gameover = True
        elif len(self.living_impostors) == 0:
            print('All impostors are dead! Crewmates win!')
            self.gameover = True
        elif len(self.tasks_remaining) > 0:
            print(f'{len(self.living_impostors)} impostors remain')
            print(str(len(self.tasks_remaining)) + ' tasks remain')
            for x in self.living_crewmates:
                name = x.name
                print(name)
        else:
            for x in self.living_crewmates:
                x.roam()
                print(x.location)
        # print(self.living_impostors[0].color)



    def call_meeting(self):
        vote = input('Who do you think is the impostor?\n')
        for x in self.living_impostors:
            if vote == x.name:
                self.living_impostors.remove(x)
                x.is_alive = False
        self.game_status()

    def lets_go(self):
        print('Game running!')
        while self.gameover == False:
            for _ in range(0, 4):
                if self.meet == False:
                    self.imp.roam()
                    # for x in self.living_impostors:
                    #     x.roam()
                    self.murder_check()
            if self.meet == True and len(self.living_crewmates) > 0 and len(self.tasks_remaining) > 0:
                self.call_meeting()
                self.meet = False
            else:
                self.game_status
            self.move_crewies()

        
if __name__ == "__main__":
    polus = Spaceship()
    polus.setup_game()
    polus.lets_go()
    
