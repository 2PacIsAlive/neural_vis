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
    print weights[data][0].shape()
