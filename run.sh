#!/bin/bash
python encodeData.py ./data/train.json
mv encoding_output.mat ./data/train_encoded.mat
python encodeData.py ./data/test.json
mv encoding_output.mat ./data/test_encoded.mat

cd ./classifiers

echo "Result from svm algorithm is:"
python svm.py

echo "Result from logistic regression is:"
python logistic_regression.py

cd ..