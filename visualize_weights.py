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
	#v = str(int(value * 100000))
	#while len(v) < 6:
	#	v += '0'
	#return int(v[:2], 16), int(v[2:4], 16), int(v[4:6], 16)
	value *= 255
	return int(value), int(value), int(value) 
'''
for file_ in glob('data/weights/*'):
	print "loading", file_
	data = np.load(file_)
	weights[file_] = data
''' 

#for data in weights:
for file_ in glob('data/weights/*'):
	data = np.load(file_)
	layer_counter = 0
	for layer in data:
		if layer_counter == 0: # only doing the input layer right now
			#for dim_counter, dim in enumerate(layer):
			#img_hi = Image.new( 'RGB', (layer.shape[0],layer.shape[1]), "black")
			img_hi = Image.new( 'RGB', (int(math.pow(layer.shape[1], .5)), int(math.pow(layer.shape[1], .5))), "black")
			pixels_hi = img_hi.load()
			counter = 0
			image = layer[0]
			for i in range(img_hi.size[0]):
				for j in range(img_hi.size[1]):
					pixels_hi[i,j] = getHexValue(image[counter])
					counter += 1	
			img_hi.save('gradient_ascent_images/png/it' + file_[13:-4] + '_' \
					+ layer_lookup[layer_counter] + '.png','png')
			#dim_counter += 1
		layer_counter += 1

			#os.system('convert gradient_ascent_images/png/*.png animations/gradient_ascent_test.mpeg')
			#os.system('convert layer_images/png/*.png			 animations/hidden_unit_0.mpeg')
			#os.system('open animations/gradient_ascent_test.mpeg')
			#os.system('open animations/hidden_unit_0.mpeg')

