import random


# class Ghost(object):
#     colors = ['white', 'yellow', 'purple', 'red']

#     def __init__(self):
#         self.color = self.colors[random.randint(0, 3)]

class Ghost(object):
    colors = ['white', 'yellow', 'purple', 'red']

    def __init__(self):
        self.color = random.choice(Ghost.colors)
