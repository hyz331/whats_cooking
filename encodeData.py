# This file uses wordMap and cuisineMap to perform oneHotEncoding, and
# save it into matlab format.

import json
import numpy as np
import scipy.io as sio
import sys

if (len(sys.argv) <= 1):
	print 'Usage:', sys.argv[0], 'filename.json'
	print 'A file named encoding_output.mat will be created in the current directory'
	sys.exit()

def getWords(item):
	words = set()
	for ingredients in item['ingredients']:
		ingredients = ingredients.split(' ')
		for w in ingredients:
			if (len(w) >= 3 and w.isalpha()):
				words.add(w)
	return list(words)

# Load mappings
filename = sys.argv[1]
wordMap = json.loads(open(filename).read())
cuisineMap = json.loads(open('data/cuisineMap.json').read())
data = json.loads(open('data/train.json').read())

# Perform encoding
numFeature = len(wordMap)
numClass = len(cuisineMap)

features = []
labels = []
total = len(data)
count = 0
for item in data:
	feature = [0 for i in range(0, numFeature)]
	words = getWords(item)
	for w in words:
		if (w in wordMap): feature[wordMap[w]] = 1
	features.append(feature)
	if ('cuisine' in item):
		labels.append(cuisineMap[item['cuisine'].lower()])	
	count = count + 1
	print count, "/", total

# Save data
features = np.array(features)
labels = np.array(labels)
sio.savemat('encoding_output.mat', {'features': features, 'labels': labels})
