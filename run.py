import os
import time

from Game import Game
from Qbot import Qbot

# Clears Terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Prints Game Board
def visualize(s):
    print("-"*30)
    print("")
    for row in s:
        srow = ""
        for e in row:
            srow = srow + e + " "
        print(srow)
    print("")
    print("-"*30)
        
# Enviornment
env = Game()
qbot = Qbot(env.action_space, env.size, )



#Trainning
for i in range(100):
    done  = False
    qbot.clear()
    while(not done):
        # Runs action on Environment
        a = qbot.act(env.apos)
        s, r, done = env.step(a)
        
        # Displays move taken
        clear()
        visualize(s)
        print(a)

        # Calculates running Qval
        qbot.updateQval(r)

    print("Trial: " + str(i))
    qbot.updateQtable()
    env.reset()

#Testing
clear()
print("Testing")
time.sleep(3)

qbot.clear()
done  = False
qbot.egreedy = 1

while(not done):
    # Runs action on Environment
    a = qbot.act(env.apos)
    s, r, done = env.step(a)
    
    # Displays move taken
    clear()
    visualize(s)
    print(a)
    time.sleep(2)

    # Calculates running Qval
    qbot.updateQval(r)

print("Trial: " + str(i))
qbot.updateQtable()