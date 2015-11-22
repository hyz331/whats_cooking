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

print "Run SVM"
m = svm_train(labels, features)
svm_save_model('svm_trained.model', m)
