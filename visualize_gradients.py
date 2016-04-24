#!usr/bin/env python

import matplotlib.pyplot as plt
import multiprocessing
from glob import glob
import numpy as np

def save_image(filename):
    grads = np.load(filename)	
    
    iname = filename.replace('.npy','.png')
    print "saving", iname
    
    fig = plt.figure(figsize=(15,15))
    axes = plt.gca()
    axes.set_ylim([-0.01,0.01])
    axes.set_axis_bgcolor('black')
    plt.plot(grads)

    fig.savefig(iname,dpi=80,bbox_inches='tight')
    plt.close()

pool = multiprocessing.Pool(multiprocessing.cpu_count())
for filename in glob('data/gradients/intercept/*'):
    pool.apply_async(save_image, (filename,))
pool.close()
pool.join()
