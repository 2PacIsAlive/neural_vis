import os
import numpy as np
from mayavi import mlab
import mayavi

def creator(name, curDir):
    saveName = name.split('.')[0]
    data = np.load(curDir+'/'+name)
    plotter = np.array([data[0]]).reshape(160,160)*255
    mlab.barchart(plotter, auto_scale=False, reset_zoom=False)
    mlab.savefig('../../mayaHist/'+saveName+'.png')

os.chdir('/home/parallels/Desktop/Parallels Shared Folders/Home/neural_vis/data/weights')
curDir = '/home/parallels/Desktop/Parallels Shared Folders/Home/neural_vis/data/weights'
for name in [x for x in os.listdir(curDir) if x.endswith('.npy')]:
    #mayavi.new_scene()
    creator(name, curDir)
    mlab.close(all=True)
