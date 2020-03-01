import random as rd
from time import sleep


class bear:
    def __init__(self):
        self.gender = rd.choice(['F.', 'M.'])
        self.strangth = rd.randint(1, 9)
        self.move = 0

    def __getitem__(self):
        return self.move

    def mov(self):
        self.move = 1

    def one_later(self):
        self.move = 0

class fish:
    def __init__(self):
        self.gender = rd.choice(['F.', 'M.'])
        self.strangth = rd.randint(1, 9)
        self.move = 0

    def __getitem__(self):
        return self.move

    def mov(self):
        self.move = 1

    def one_later(self):
        self.move = 0

class ecosystem:
    def __init__(self, bears=2, fish=2, river_size=None):
        num = bears + fish
        if river_size == None or river_size < num:
            print("river size is too small!")
            river_size = num
        self.bears = bears
        self.fish = fish
        self.river_size = river_size
        self.make_new_river()
        self.Year = 0
        self.print_river()

    def make_new_river(self):
        river_size = self.river_size - self.bears - self.fish
        self.river = [None] * river_size
        for _ in range(self.bears):
            self.river.append(bear())
        for _ in range(self.fish):
            self.river.append(fish())
        rd.shuffle(self.river)
        print(self.river)

    def make(self, animal):
        if self.river.count(None) > 0:
            if rd.randint(0,1) == 1:
                index = [i for i, _ in enumerate(self.river) if _ == None]
                self.river[rd.choice(index)] = animal

    def act(self):
        acts = [i for i, _ in enumerate(self.river) if _ != None]
        act = self.river.copy()
        for i in acts:
            act[i] = rd.randint(-1, 1)
            if act[i] == 0:
                act[i] = None
        return act

    def system(self, i, act):
        animal = self.river[i]
        animals = type(self.river[i])
        moved = animal
        if act != 0 and moved != 1:
            move = i + act
            if move >= 0 and move < self.river_size:
                if self.river[move] == None:
                    self.river[move] = self.river[i]
                    self.river[i] = None
                elif type(self.river[move]) == animals:
                    if animal.gender != self.river[move].gender:
                        if animals == bear:
                            self.make(bear())
                        else:
                            self.make(fish())
                    else:
                        if animal.strangth > self.river[move].strangth:
                            self.river[move] = self.river[i]
                        self.river[i] = None
                else:
                    if animals != bear:
                        self.river[i] = None
                    else:
                        self.river[i].hunger = -1
                        self.river[move] = self.river[i]
                        self.river[i] = None
            animal.mov()


    def strat(self, act_time=10):
        time = 0
        while time != act_time:
            act = self.act()
            order = [i for i, _ in enumerate(act) if _ != None]
            rd.shuffle(order)
            for i in order:
                self.system(i, act[i])
            time += 1
            [x.one_later() for x in self.river if x != None]
            sleep(0.8)
            self.print_river()

    def print_river(self):
        s = '|'
        for x in self.river:
            if x:
                if type(x) == bear:
                    s += 'B.'
                elif type(x) == fish:
                    s += 'F.'
                s += x.gender
                s += str(x.strangth)
            else:
                s += '     '
            s += '|'
        print('='*13 + ' ' + str(self.Year) + ' 년' + '='*300)
        print(s)
        print('='*350)
        self.Year += 1

river = ecosystem(5,15,30)
river.strat(50)