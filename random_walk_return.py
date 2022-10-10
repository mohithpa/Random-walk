from random import random
import numpy as np
import matplotlib.pyplot as plt

x = [0]
y = [0]

all_steps = [[0,1],[1,0],[0,-1],[-1,0]]

def random_step_generator(steps_list):
    random_step = np.random.choice([0,1,2,3])
    a = steps_list[random_step]
    return a

for i in range(20000):
    step = random_step_generator(all_steps)
    x.append(step[0]+x[-1])
    y.append(step[1]+y[-1])
    
plt.plot(x,y)    
plt.savefig("random_path.png")
