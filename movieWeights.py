#!/usr/bin/env python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.image as mgimg
import os

fig = plt.figure()
ax = plt.gca()

nDir = '/Users/paul/neural_vis/mayaHist/'
names = os.listdir(nDir)

def init():
	imobj.set_data(np.zeros((160,160)))
	return imobj,

def animate(i):
	fname = names[i]

	img = mgimg.imread(fname)[-1:-1]
	imobj.set_data(img)

	return imobj,

imobj = ax.imshow( np.zeros((100, 100)), origin='lower', alpha=1.0, zorder=1, aspect=1 )

anim = animation.FuncAnimation(fig, animate, init_func=init, repeat=True, \
		frames=range(1,4), interval=200, blit=True, repeat_delay=1000)

plt.show()
