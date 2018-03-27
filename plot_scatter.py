import numpy as np
import matplotlib.pyplot as plt
import pickle
import gym
from colour import Color

goals = pickle.load(open('hardmaze_es/goals.pkl','rb'))
goals = np.array(goals)
env = gym.make("HardMaze-v0")
obs = env.reset()
env.render()
blue = Color("blue")
colors = list(blue.range_to(Color("red"), goals.shape[0]))
colors = [c.get_rgb() for c in colors]
plt.scatter(goals[:,0], goals[:,1], marker='x', c=colors)
plt.show()
