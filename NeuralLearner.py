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
            self.testing_expected  = [packet[1] for packet in self.data.testingActivations]  # testing  labels
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
print "TRAINING"
for i in range(len(accuracy)):
    print accuracy[i], net.training_expected[i]
print "TESTING"
guess = net.Predict()
for i in range(len(guess)):
    print guess[i], net.testing_expected[i]
