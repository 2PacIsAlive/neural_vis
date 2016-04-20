#!usr/bin/env python

import glob
import numpy
import pylab
import pandas
import random
from PIL import Image

class Images:

    trainingActivations = []
    testingActivations = []

    def loadData(self):
        print "\nloading training data..."
        folders = list(glob.glob('training_images/*'))
        reps = [(list(glob.glob(folder + "/*")), folder[26:])  for folder in folders]
        for files, name in reps:
            for file_ in files:
                print file_, "loaded"
                img = Image.open(file_)
                pix = list(img.getdata())
                act = []
                for pixel in pix:
                    #hexval = hex(str(pixel)[0]) + hex(str(pixel)[1])[:1] + hex(str(pixel)[2])[:1]
                    #act_hi.append((int(hexval,16))/100000.0)
                    act.append(pixel[0]/255.0) 
                    act.append(pixel[1]/255.0) 
                    act.append(pixel[2]/255.0) 
                if random.randint(0,100) < 75:
                    self.trainingActivations.append((act, name))
                else:
                    self.testingActivations.append((act, name))
