from PIL import Image
import os
import multiprocessing


# def makeImg():
dirr = '/Users/paul/neural_vis/weight_images/imgs/'
names = os.listdir('/Users/paul/neural_vis/weight_images/imgs/')
destDir = '/Users/paul/neural_vis/weight_images/final/'
layer = []
fil = []
for name in names:
	seps = name.split('.')[0].split('_')
	if seps[0] not in fil:
		fil.append(seps[0])
	if seps[1] not in layer:
		layer.append(seps[1])

fil = [int(x) for x in fil if int(x)]
layer = [int(x) for x in layer]
fil.sort(key=int)
layer.sort(key=int)
xAll = [x for x in xrange(0,160,10)]
for i in fil:
	print 'starting '
	newName= destDir + 'inputImg_' + str(i) + '.png'
	new_im = Image.new('RGB', (160,160))
	filNames = [name for name in names if name.split('_')[0]==str(i)]
	count = 0
	for x in xAll:
		for y in xAll:
			#opens an image and saves:
			im = Image.open(dirr+filNames[count])
			new_im.paste(im, (x,y))
			count+=1

	new_im.save(newName, 'png')
	print("\tImages %s saved" %{i})
	new_im.close()
'''
pool = multiprocessing.Pool(multiprocessing.cpu_count())
for i in os.listdir('/Users/paul/neural_vis/weight_images/imgs/'):
	pool.apply_async(makeImg)
pool.close()
pool.join()
'''
