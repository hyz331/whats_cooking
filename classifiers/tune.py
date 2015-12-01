import numpy as np
import scipy.io as sio
from sklearn import svm

# Load data
print "Loading mat data"
data = sio.loadmat('../data/train_encoded.mat')
X = data['features']
Y = data['labels'][0]

# Fit model
for c in [0, 50, 100, 125, 150, 200]:
	classifier = svm.SVC(C = 150)
	print 'training...'
	classifier.fit(X[1:10000], Y[1:10000])
	print 'predicating...'
	print c, classifier.score(X[20000:30000], Y[20000:30000])
