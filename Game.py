class Game:
    def __init__(self,size=3):
        self.size = size
        self.action_space = 4
        self.gstate = [['o' for i in range(self.size)] for j in range(self.size)]
        self.apos = (0,0)
        self.hpos = (1,1)
        self.spos = (2,2)

        self.gstate[self.apos[0]][self.apos[1]] = 'A'
        self.gstate[self.hpos[0]][self.hpos[1]] = '#'
        self.gstate[self.spos[0]][self.spos[1]] = '*'
        
        self.steps = 0

    def reset(self):
        self.gstate = [['o' for i in range(self.size)] for j in range(self.size)]
        self.apos = (0,0)
        self.hpos = (1,1)
        self.spos = (2,2)

        self.gstate[self.apos[0]][self.apos[1]] = 'A'
        self.gstate[self.hpos[0]][self.hpos[1]] = '#'
        self.gstate[self.spos[0]][self.spos[1]] = '*'
        
        self.steps = 0

    def amove(self,pos):
        if((pos[0] < self.size and pos[0] >= 0) and (pos[1] < self.size and pos[1] >= 0)):
            if(self.apos != self.hpos and self.apos != self.spos):
                self.gstate[self.apos[0]][self.apos[1]] = 'x'
            elif(self.apos == self.hpos):
                self.gstate[self.apos[0]][self.apos[1]] = '#'
            else:
                self.gstate[self.apos[0]][self.apos[1]] = '*'

            self.apos = pos
            self.gstate[self.apos[0]][self.apos[1]] = 'A'
    
    def getreward(self):
        if(self.apos != self.hpos and self.apos != self.spos):
            return 0
        elif(self.apos == self.hpos):
            return -1
        else:
            return 10
    
    def moveright(self): 
        pos = self.apos
        pos = (pos[0] + 1, pos[1])
        self.amove(pos)

    def moveleft(self):
        pos = self.apos
        pos = (pos[0] - 1, pos[1])
        self.amove(pos)

    def moveup(self):
        pos = self.apos
        pos = (pos[0], pos[1] + 1)
        self.amove(pos)
    
    def movedown(self):
        pos = self.apos
        pos = (pos[0], pos[1] - 1)
        self.amove(pos)

    def step(self,a):
        done = False
        actions = {
            0 : self.moveright,
            1 : self.moveleft,
            2 : self.moveup,
            3 : self.movedown
        }

        actions[a]()
        if(self.steps >= 5):
            done = True
        self.steps = self.steps + 1
        return self.gstate, self.getreward(), done