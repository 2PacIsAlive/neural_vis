#!usr/bin/env python

from PIL  import Image
from glob import glob
from matplotlib.colors import rgb2hex
import json
import os

class Generator:
    def __init__(self):
        for file_ in glob('gradient_ascent_images/json/*'):
            img_hi = Image.new( 'RGB', (32,32), "black")
            img_lo = Image.new( 'RGB', (32,32), "black")
            pixels_hi = img_hi.load()
            pixels_lo = img_lo.load()
            counter = 0
            with open(file_, 'r') as gradient_ascent_image:
                gradient_ascent_image = json.load(gradient_ascent_image)
                
                for i in range(img_hi.size[0]):
                    for j in range(img_hi.size[1]):
                        pixels_hi[i,j] = self.getHexValue(gradient_ascent_image['hi'][counter])
                        counter += 1    

                counter = 0
                for i in range(img_lo.size[0]):
                    for j in range(img_lo.size[1]):
                        pixels_lo[i,j] = self.getHexValue(gradient_ascent_image['lo'][counter])
                        counter += 1
            img_lo.save('gradient_ascent_images/png/' + file_[28:-5]+'lo.png','png')
            img_hi.save('gradient_ascent_images/png/' + file_[28:-5]+'hi.png','png')
        for file_ in glob('layer_images/json/*'):
            img_hi = Image.new( 'RGB', (11,11), "black")
            pixels_hi = img_hi.load()
            counter = 0
            with open(file_, 'r') as gradient_ascent_image:
                gradient_ascent_image = json.load(gradient_ascent_image)
                for i in range(img_hi.size[0]):
                    for j in range(img_hi.size[1]):
                        pixels_hi[i,j] = self.getHexValue(gradient_ascent_image[counter])
                        counter += 1
            img_hi.save('layer_images/png/' + file_[28:-5]+'hi.png','png')
            img_lo.save('layer_images/png/' + file_[28:-5]+'lo.png','png')
        #os.system('convert gradient_ascent_images/png/*.png animations/gradient_ascent_test.mpeg')
        #os.system('convert layer_images/png/*.png           animations/hidden_unit_0.mpeg')
        #os.system('open animations/gradient_ascent_test.mpeg')
        #os.system('open animations/hidden_unit_0.mpeg')

    def getHexValue(self, value):
        print value
        v = str(int(value * 100000))
        while len(v) < 6:
            v += '0'
        return int(v[:2], 16), int(v[2:4], 16), int(v[4:6], 16)


def main():
    G = Generator()

if __name__ == '__main__': main()
