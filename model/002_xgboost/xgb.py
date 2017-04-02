#!/usr/local/bin/python
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import log_loss
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import KFold

def run_xgb(train, features, target):
    #parameters
    params = {}
    params["objective"]         = "binary:logistic"
    params["eval_metric"]       = "logloss"
#    params["booster"]           = "gbtree"
    params["eta"]               = 0.02
#    params["tree_method"]       = 'exact'
    params["max_depth"]         = 4
#    params["subsample"]         = 0.8
#    params["colsample_bytree"]  = 0.8
    params["silent"]            = 1
#    params["nthread"]           = 4
#    params["seed"]              = 0
#    params["scale_pos_weight"]  = 0.8

    X_train, X_valid = train_test_split(train, test_size=0.20, random_state=0)
    del train
    
    y_train = X_train[target]
    y_valid = X_valid[target]
    dtrain = xgb.DMatrix(X_train[features], y_train)
    dvalid = xgb.DMatrix(X_valid[features], y_valid)
    del X_train, X_valid, y_train, y_valid
    
    watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
    gbm = xgb.train(params, dtrain, 20000, evals=watchlist,
    		early_stopping_rounds=50, verbose_eval=100)

    del dtrain, dvalid
    
    return gbm

#nrows=400000

path = "../../numeric/"
df = pd.read_csv(path+"train_numeric.csv")#,nrows=nrows)

target = "is_duplicate"
features = list(df.columns.values)
features.remove(target)

kf = KFold(len(df.index),3)
scores = []
for train_index, test_index in kf:
    train, valid = df.iloc[train_index,:], df.iloc[test_index,:]
    gbm = run_xgb(train,features,target)
    Y = gbm.predict(xgb.DMatrix(valid[features]),ntree_limit=gbm.best_iteration)
    score = log_loss(valid[target],Y)
    scores.append(score)
print np.mean(scores), np.std(scores)
