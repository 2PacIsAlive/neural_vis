import os


os.chdir('./weight_images/png/')
origDir = os.getcwd()+'/'
newDir = '/'.join(origDir.split('/')[:-2])+'/imgs/'
names = os.listdir('.')
finalNames = []
for name in names:
	seps = name.split('.')[0].split('_')
	layer = seps[0]
	fil = seps[1]
	finalNames.append(newDir + str(fil) + '_' + str(layer) \
											+ '_input.png')
for name,finName in zip(names, finalNames):
	os.rename(name, finName)
