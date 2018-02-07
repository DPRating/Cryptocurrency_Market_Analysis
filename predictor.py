import numpy as np
import pandas as pd
from DecisionTreeClassifier import train

input_path = './data/inputs'
classifier_path = './classifier'
# features = 

if __name__ == "__main__":
    with open(classifier_path, 'rb') as f:
        clfs = pickle.load(f)
    values = []
    for clf in clfs:
        values.append(clf.predict(features)[0])
        
    print(np.mean(values))





