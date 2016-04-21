import matplotlib.pyplot as plt
import numpy as np

from glob import glob

weights = {}

for file_ in glob('images/*.npy'):
    data = np.load(file_)
    if 'weights' in file_:
        weights[file_] = data
    
for data in weights:
    for layer in weights[data]:
        print layer.shape
