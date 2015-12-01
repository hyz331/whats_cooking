import numpy as np
import scipy.io as sio
from sklearn import linear_model

# Load data
print "Loading mat data"
data = sio.loadmat('../data/train_encoded.mat')
X = data['features']
Y = data['labels'][0]

# Fit model
print "Training..."
for reg in [10, 25, 50, 100, 150, 200]:
	classifier = linear_model.LogisticRegression(C = reg)
	classifier.fit(X[1:30000], Y[1:30000])
	print reg, classifier.score(X[30000:39774], Y[30000:39774])
