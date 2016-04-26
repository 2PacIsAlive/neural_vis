from __future__ import division
import sys
import numpy as np
from sklearn.neural_network import MLPClassifier
from image_loader import Images

class NeuralLearner:
	def __init__(self):
			self.data = Images()
			self.data.loadData()
			self.training_expected = [packet[1] for packet in self.data.trainingActivations] # training labels
			self.testing_expected  = [packet[1] for packet in self.data.testingActivations]  # testing	labels
			self.model = MLPClassifier(algorithm = str(sys.argv[3]), 
									   shuffle = True,
									   learning_rate = str(sys.argv[2]),
									   momentum = .9,
									   nesterovs_momentum = True, 
									   max_iter=int(sys.argv[1]))
			
	def Fit(self):
			arr = [pix for pix, label in self.data.trainingActivations]
			self.model.fit(arr, self.training_expected)
			return self.model.predict(arr)

	def Predict(self):
			arr = [pix for pix, label in self.data.testingActivations]
			return self.model.predict(arr)

def saveScores(accPercent):
	doc = open('./scores.txt', 'a')
	doc.write(str(sys.argv[1])+'\t'+str(sys.argv[2])+'\t'+str(sys.argv[3])+'\t'+str(accPercent)+'\n')

corr = 0
net = NeuralLearner()
accuracy = net.Fit()
print "TRAINING"
for i in range(len(accuracy)):
	if accuracy[i] != net.training_expected[i]: errors += 1
print "TESTING"
guess = net.Predict()
for i in range(len(guess)):
	if guess[i] == net.testing_expected[i]:
		corr+=1
saveScores(float(corr/len(guess)))
