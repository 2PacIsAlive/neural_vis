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
    v = str(int(value * 100000))
    while len(v) < 6:
        v += '0'
    return int(v[:2], 16), int(v[2:4], 16), int(v[4:6], 16)

for file_ in glob('images/weights*'):
    print "loading", file_
    data = np.load(file_)
    weights[file_] = data
    
for data in weights:
    layer_counter = 0
    for layer in weights[data]:
        if layer_counter == 0: # only doing the input layer right now
            with open(file_, 'r') as gradient_ascent_image:
                dim_counter = 0
                for dim in gradient_ascent_image:
                    #img_hi = Image.new( 'RGB', (layer.shape[0],layer.shape[1]), "black")
                    img_hi = Image.new( 'RGB', (int(math.pow(layer.shape[1], .5)), int(math.pow(layer.shape[1], .5))), "black")
                    pixels_hi = img_hi.load()
                    counter = 0
                    image = layer[dim_counter]
                    for i in range(img_hi.size[0]):
                        for j in range(img_hi.size[1]):
                            pixels_hi[i,j] = getHexValue(image[counter])
                            counter += 1    
                    img_hi.save('gradient_ascent_images/png/' + file_[28:-5]+ str(dim_counter) + '_' + layer_lookup[layer_counter] + '.png','png')
                    dim_counter += 1
        layer_counter += 1

            #os.system('convert gradient_ascent_images/png/*.png animations/gradient_ascent_test.mpeg')
            #os.system('convert layer_images/png/*.png           animations/hidden_unit_0.mpeg')
            #os.system('open animations/gradient_ascent_test.mpeg')
            #os.system('open animations/hidden_unit_0.mpeg')

