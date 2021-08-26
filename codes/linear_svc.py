#!/usr/bin/env python
# coding: utf-8

from sklearn.model_selection import train_test_split 
from sklearn.model_selection import ShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from numpy import load

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define the variables of my model
data = np.load('schaefern100_features.npz')
X_features = data['conn'] 
y_group = data['cond']

# Model fitting 
X, X_test, y, y_test = train_test_split(
     X_features,        # x
     y_group,           # y
     train_size=0.75,   # 75%/25% split                                                 
     test_size = 0.25,  
     shuffle = True,    # shuffle dataset before splitting
     stratify = y_group, 
     random_state = 123 # same shuffle every run for reproducibility
)
print('Number of participants:\n')
print('training:', len(X),
     'testing:', len(X_test))
print('\n')

cv = ShuffleSplit(n_splits=5, test_size=.3, random_state=0)
pca = PCA(0.95)
X = np.vstack(X_features)
y = y_group = np.array(y_group)

val_accuracies = []
train_accuracies = []
model = []
i=0

# Tuning the hyper-parameters of an estimator for optimization
for train, val in cv.split(X, y):
    X_train, X_val = X[train], X[val]
    y_train, y_val = y[train], y[val]
    
    pipe = Pipeline(steps=[('standardscaler', StandardScaler()),
                           ('feature_selection', pca),('linearsvc', SVC(kernel='linear', C=1))])
    
    pipe.fit(X_train, y_train)                  # fit to training data
    y_val_pred = pipe.predict(X_val)            # classify the condition group using validation set    
    
    model.append(pipe['feature_selection'].inverse_transform(pipe['linearsvc'].coef_))

    # get accuracy
    val_accuracies.append(pipe.score(X_val, y_val)) 
    train_accuracies.append(pipe.score(X_train, y_train))

    # confusion matrix for all splits
    val_matrix = confusion_matrix(y_val, y_val_pred, labels=['control', 'deaf'], normalize='true')
    plt.figure()
    heatmap = sns.heatmap(val_matrix, vmin = 0, vmax = 1, annot = True, cmap = 'YlGnBu')
    heatmap.figure.savefig(f'confusion_matrix_{i}.png')
    i = i+1
     
# Verify the classification on the test set
train_val = pipe.fit(X, y) # fit to the train and validation sets

test_accuracies = train_val.score(X_test, y_test) 
y_test_pred = train_val.predict(X_test)

# Score metrics
train_accuracies = np.array(train_accuracies)
val_accuracies = np.array(val_accuracies)
test_accuracies= np.array(test_accuracies)

print('Accuracy scores (mean ± std) for: \n')
print(f' - Train set = {train_accuracies.mean()} ± {train_accuracies.std()}')
print(f' - Validation set = {val_accuracies.mean()} ± {val_accuracies.std()}\n')
print(f' - Test set = {test_accuracies.mean()} ± {test_accuracies.std()}')
