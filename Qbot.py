import numpy as np
from random import randint

class Qbot:
    def __init__(self, action_space, env_size):

        self.action_space = action_space
        self.env_size = env_size

        # Initilizing Q-Table
        self.Qtable = [[[0 for k in range(action_space)] for i in range(env_size)] for j in range(env_size)] 

        # Hyperparameters
        self.gamma = 1
        self.egreedy = 0.5
        self.egreedy_increment = 0.01

    def clear(self):
        # Initilizing Variables start of the game
        self.Qval = 0
        self.memory = []
        
    def act(self, s):
        a = None
        # Determines best or random action  by egreedy
        if((float)(randint(0, 1000)) < self.egreedy * 1000):
            a = np.argmax(np.array(self.Qtable[s[0]][s[1]]))
        else:
            a = randint(0, self.action_space - 1)

        # Appends to this trials memory
        self.memory.append([int(a),s])
        return a
    
    def updateQval(self, r):
        self.Qval = self.Qval + (r * self.gamma)

    def updateQtable(self):
        # Updating Q-Table
        for m in self.memory:
            if(self.Qtable[m[1][0]][m[1][1]][m[0]] < self.Qval):
                self.Qtable[m[1][0]][m[1][1]][m[0]] = self.Qval

        # Updating egreedy
        if(self.egreedy < 0.75):
            self.egreedy = self.egreedy + self.egreedy_increment
        
        print("egreedy: " + str(self.egreedy))
        print("Score: " + str(self.Qval))
        print("Qtable: " + str(self.Qtable))
    

    