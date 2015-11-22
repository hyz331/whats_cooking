# This files reads the original Kaggle JSON training file, and genreate a dictionary
# that maps each word to an integer

import json

# Load JSON data
json_data = open('data/train.json').read()
data = json.loads(json_data)

# Get all ingredients/cuisines
words = set()
cuisines = set()
for item in data:
	cuisines.add(item['cuisine'].lower())
	for ingredients in item['ingredients']:
		ingredients = ingredients.split(' ')
		for w in ingredients:
			if (len(w) >= 3 and w.isalpha()):
				words.add(w.lower())

# Sort ingredient/cuisines in alphabetical order
words = list(words)
words.sort()
cuisines = list(cuisines)
cuisines.sort()

# Generate reverse mapping
wordMap = dict()
for i in range(0, len(words)):
	wordMap[words[i]] = i

cuisineMap = dict()
for i in range(0, len(cuisines)):
	cuisineMap[cuisines[i]] = i

# Dump mappings into JSON
with open('data/wordMap.json', 'w') as fp:
    json.dump(wordMap, fp)

with open('data/cuisineMap.json', 'w') as fp:
    json.dump(cuisineMap, fp)
