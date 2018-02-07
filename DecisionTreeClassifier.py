import numpy as np
import pandas as pd
import read_data
from sklearn.tree import DecisionTreeClassifier

input_path = './data/inputs'
classifier_path = './classifier'

data, labels = read_data.feature_extract(input_path)

def train(data, labels, classifier_path, num_of_trees=9, max_features=0.9):
    clfs = {i:DecisionTreeClassifier(max_features=max_features) for i in range(num_of_trees)}
    for i in range(num_of_trees):
        # feed random data
        # x = 
        # y = 
        clfs[i].fit(x, y)
    with open(classifier_path, 'wb') as f:
        pickle.dump(clfs, f)
    return



