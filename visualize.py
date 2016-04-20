import matplotlib.pyplot as plt
import numpy as np

from glob import glob

for file_ in glob('images/*.npy'):
    print file_, np.load(file_)
