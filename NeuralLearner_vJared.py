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
			self.model = MLPClassifier(algorithm = 'sgd', 
									   shuffle = True,
									   learning_rate = 'constant',
									   momentum = .9,
									   nesterovs_momentum = True, 
									   learning_rate_init = 0.2)
	   
	def Fit(self):
		arr = [pix for pix, label in self.data.trainingActivations]
		self.model.fit(arr, self.training_expected)
		return self.model.predict(arr)

	def Predict(self):
		arr = [pix for pix, label in self.data.testingActivations]
		return self.model.predict(arr)

net = NeuralLearner()
accuracy = net.Fit()
corr = 0
errors = 0
print "TRAINING"
for i in range(len(accuracy)):
	if accuracy[i] != net.training_expected[i]:	errors += 1
print "missed", errors, "out of", len(accuracy)
print "TESTING"
guess = net.Predict()
for i in range(len(guess)):
	if str(guess[i]) == str(net.testing_expected[i]):	corr+=1
print(float(corr/len(guess)))
