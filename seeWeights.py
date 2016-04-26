import matplotlib.pyplot as plt
import numpy as np
from PIL  import Image
from glob import glob
from matplotlib.colors import rgb2hex
import json
import os
from glob import glob
import math

weights = {}

layer_lookup = ['input', 'hidden-1', 'hidden-2', 'output']

def getHexValue(value):
	value *= 255
	return int(value), int(value), int(value) 

#for data in weights:
for file_ in glob('data/weights/*'):
	data = np.load(file_)
	iteration = 0
	for layer in data[0]:
		img_hi = Image.new( 'RGB', (int(math.pow(layer.shape[0], .5)), \
								int(math.pow(layer.shape[0], .5))), "black")
		pixels_hi = img_hi.load()
		image = layer.reshape(img_hi.size[0], img_hi.size[1])
		for i in range(img_hi.size[1]):
			for j in range(img_hi.size[0]):
				pixels_hi[j,i] = getHexValue(image[j,i])
				img_hi.save('gradient_ascent_images/png/' + str(iteration)\
						+ '_' + file_[13:-4] + '_' + layer_lookup[0] + '.png','png')
		iteration+=1
