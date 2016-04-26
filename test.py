#!/usr/bin/env python
import numpy as np
from visualize_weights import getHexValue
from PIL import Image

def jarod(data):
	arr = np.empty([10,10])
	layer_counter = 0
	for layer in data:
		xRange = 10
		yRange = 10
		if layer_counter == 0:
			counter = 0
			image=layer[0]
			for i in range(xRange):
				for j in range(yRange):
					arr[i,j] = image[counter]
					counter+=1
		layer_counter+=1
	return arr

def paul(data):
	for i, layer in enumerate(data[0]):
		image = np.array(layer).reshape([10,10])
	return image

data = np.load('/Users/paul/neural_vis/data/weights/1.npy')
j = jarod(data)
print j
p = paul(data)
print p
print j == p

