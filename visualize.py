import matplotlib.pyplot as plt
import numpy as np

from glob import glob

weights = {}

for file_ in glob('images/*.npy'):
    data = np.load(file_)
    print file_, data
    if 'weights' in file_:
        weights[file_] = data
    
for data in weights:
    plt.plot(weights[data][0] - weights[data][1], weights[data][0] - weights[data][1])
    plt.show()
    break # only do one
