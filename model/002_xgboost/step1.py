#!/usr/local/bin/python

import time
import sys
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import KFold

def run_xgb(train, features, target):
    #parameters
    params = {}
    params["objective"]         =       "reg:linear"
    params["eval_metric"]       =       "mae"
    params["booster"]           =       "gbtree"
    params["eta"]               =       0.03
    params["tree_method"]       =       'exact'
    params["max_depth"]         =       8
    params["subsample"]         =       0.8
    params["colsample_bytree"]  =       0.8
    params["silent"]            =       1
    params["nthread"]           =       4
    params["seed"]              =       0

    X_train, X_valid = train_test_split(train, test_size=0.20, random_state=0)#int(time.time()%100*100))
    del train
    
    y_train = X_train[target]
    y_valid = X_valid[target]
    dtrain = xgb.DMatrix(X_train[features], y_train)
    dvalid = xgb.DMatrix(X_valid[features], y_valid)
    del X_train, X_valid, y_train, y_valid
    
    watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
    gbm = xgb.train(params, dtrain, 20000, evals=watchlist,
    		early_stopping_rounds=30, verbose_eval=30)

    del dtrain, dvalid
    
    return gbm


path = "/home/guoli/work/learn_all/"

f = open("numfeas.dat","r")
lines = f.readlines()
f.close()

cols1 = []
cols2 = []
for line in lines[:400]:
    col = line.split()[0]
    if len(col.split("_"))>2:
        cols2.append(col)
    else:
        cols1.append(col)


path = "/home/guoli/work/learn_all/"
trainpath = path+"input/train.csv"

pearpath = "../../11192016_pearson/001_cat/train_pearson.csv"
bipath = "../001_getdata/train_2cat_bool.csv"
paths = [pearpath,bipath]
dts = ["float32",bool]
colses = [cols1,cols2]

df = pd.read_csv(trainpath,usecols=["loss"])
df.loss = np.log(df.loss+200)

for path, cols in zip(paths,colses):
    tmp = pd.read_csv(path,usecols=cols)
    df = pd.concat([df,tmp],axis=1)
    del tmp
#######

target = "loss"
features = list(df.columns.values)
features.remove(target)

kf = KFold(len(df.index),5)
scores = []
for train_index, test_index in kf:
    train, test = df.iloc[train_index,:], df.iloc[test_index,:]
    gbm = run_xgb(train,features,target)
    Y = gbm.predict(xgb.DMatrix(test[features]),ntree_limit=gbm.best_iteration)
    score = mean_absolute_error(np.exp(test[target]),np.exp(Y))
    print score
    scores.append(score)

print scores
print np.mean(scores),np.std(scores)
