import sys
import numpy as np
import scipy.io as sio
sys.path.append("../libsvm-3.20/python")
from svmutil import *

print "Loading mat data"
data = sio.loadmat('../data/train_encoded.mat')
features = data['features']
labels = data['labels'][0]

print "Converting into Python lists"
features = features.tolist()
labels = labels.tolist()

print "Running linear SVM with regularization"
res = []
for c in [10, 30, 50, 100, 120, 140, 160, 180, 200, 300]:
	accu = svm_train(labels[1:2000], features[1:2000], '-v 5 -c ' + str(c))
	res.append((c, accu))

print res
#m = svm_train(labels, features)
#svm_save_model('svm_trained.model', m)
