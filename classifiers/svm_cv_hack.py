import numpy as np
import scipy.io as sio
from sklearn import svm

# Load data
print "Loading mat data"
data = sio.loadmat('../data/train_encoded.mat')
X = data['features']
Y = data['labels'][0]

# Fit model
print "Training..."
classifier = svm.SVC()
classifier.fit(X[1:5000], Y[1:5000])
print "Predicting.."
print 0
print "Accuracy: ", classifier.score(X[4300:5300], Y[4300:5300])


print "Training..."
for c in [50, 100, 150, 200, 250]: 
	classifier = svm.SVC(C = c)
	classifier.fit(X[1:5000], Y[1:5000])


	print "Predicting.."
	print c
	print "Accuracy: ", classifier.score(X[4300:5300], Y[4300:5300])