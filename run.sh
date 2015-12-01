#!/bin/bash
python encodeData.py ./data/train.json
cd ./classifiers

echo "Result from svm algorithm is:"
python svm.py
echo "Result from logistic regression algorithm is:"
python logistic_regression.py

cd ..