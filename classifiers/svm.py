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
classifier = svm.SVC(C = 150)
classifier.fit(X[1:1000], Y[1:1000])


print "Predicting.."
print "Accuracy: ", classifier.score(X[1000:2000], Y[1000:2000])
