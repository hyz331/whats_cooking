import numpy as np
import scipy.io as sio
from sklearn import linear_model

# Load data
print "Loading mat data"
data = sio.loadmat('../data/train_encoded.mat')
X = data['features']
Y = data['labels'][0]
testData = sio.loadmat('../data/test_encoded.mat')
testX = testData['features']
ids = testData['ids']
 
# Fit model
print "Training..."
classifier = linear_model.LogisticRegression()
classifier.fit(X, Y)
prediction = classifier.predict(testX)

# Print train accuracy
print classifier.score(X, Y)

# Save data
testId = ids.tolist()
predicts = prediction.tolist()
sio.savemat('../lr_prediction.mat', {'ids': ids, 'predicts': predicts})
