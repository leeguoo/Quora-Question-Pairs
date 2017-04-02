#!/usr/local/bin/python
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import log_loss
from sklearn.cross_validation import train_test_split, KFold
from sklearn.ensemble import RandomForestRegressor

nrows=100000

path = "../../numeric/"
df = pd.read_csv(path+"train_numeric.csv",nrows=nrows)

target = "is_duplicate"
features = list(df.columns.values)
features.remove(target)

features.remove('WC_TFIDF')

kf = KFold(len(df.index),5)
scores = []
for train_index, test_index in kf:
    train, valid = df.iloc[train_index,:], df.iloc[test_index,:]
    rf = RandomForestRegressor(n_estimators=100)
    rf.fit(train[features],train[target])

    Y = rf.predict(valid[features])
    score = log_loss(valid[target],Y)
    scores.append(score)
print np.mean(scores), np.std(scores)
