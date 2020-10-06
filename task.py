import random

class Task:
    common_tasks = {
        'Fix Wiring': ['Admin', 'Cafeteria', 'Electrical', 'Navigation', 'Security', 'Storage'],
        'Swipe Card': ['Admin'],
        'Fuel Engines': ['Lower Engine', 'Upper Engine', 'Storage'],
        'Empty Garbage': ['Cafeteria', 'Storage'],
        'Divert Power': ['Electrical', 'Comms', 'Upper Engine','Lower Engine', 'Navigation', 'Oxygen', 'Reactor', 'Security', 'Shields'],
        'Upload Data': ['Cafeteria', 'Comms', 'Electrical', 'Navigation', 'Admin', 'Weapons'],
        'Align Engine Output': ['Upper Engine', 'Lower Engine']
    }
    # unique_tasks = [
    #     ('Inspect Sample', 'MedBay'),
    #     ('Chart Course', 'Navigation'),
    #     ('Calibrate Distributor', 'Electrical'),
    #     ('Clear Asteroids', 'Weapons'),
    #     ('Clean O2 Filter', 'Oxygen'),
    #     ('Stabilize Steering', 'Navigation'),
    #     ('Prime Shields', 'Sheilds'),
    #     ('Submit Scan', 'MedBay'),
    #     ('Start Reactor', 'Reactor'),
    #     ('Unlock Manifolds', 'Reactor')
    # ]
    unique_tasks = {
    'Inspect Sample': 'MedBay',
    'Chart Course': 'Navigation',
    'Calibrate Distributor': 'Electrical',
    'Clear Asteroids': 'Weapons',
    'Clean O2 Filter': 'Oxygen',
    'Stabilize Steering': 'Navigation',
    'Prime Shields': 'Sheilds',
    'Submit Scan': 'MedBay',
    'Start Reactor': 'Reactor',
    'Unlock Manifolds': 'Reactor'
}
    sabotage_tasks = {
        'Stop Oxygen Depletion': 'Oxygen',
        'Fix Communications': 'Comms',
        'Fix Lights': 'Electrical',
    }

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.is_completed = False

if __name__ == "__main__":
    testers = list(Task.unique_tasks.items())
    rando, blando = random.choice(testers)
    test_task = Task(rando, blando)
    print(test_task.name, test_task.location)