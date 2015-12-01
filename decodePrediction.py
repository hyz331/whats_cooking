# This script reads prediction result in mat format, and 
# format it into Kaggle submission csv

import sys
import numpy as np
import scipy.io as sio
import json

if (len(sys.argv) <= 1):
	print 'Usage', sys.argv[0], 'predict.mat'
	print 'A file named submission.csv will be created in the current directory'
	sys.exit()

# Load data and mapping
filename = sys.argv[1]
data = sio.loadmat(filename)
cuisineMap = json.loads(open('data/cuisineMap.json').read())

ids = np.transpose(data['ids']).tolist()
predicts = np.transpose(data['predicts']).tolist()
print len(predicts)


# Construct reverse mapping
revMap = dict()
for k in cuisineMap:
	if (not cuisineMap[k] in revMap):
		revMap[cuisineMap[k]] = k

# Print to file
outfile = open('submission.csv', 'w+')
print >> outfile, 'id,cuisine'
for i in range(0, len(ids)):
	print >> outfile, '%s,%s' % (ids[i][0], revMap[int(predicts[i][0])])
outfile.close()
