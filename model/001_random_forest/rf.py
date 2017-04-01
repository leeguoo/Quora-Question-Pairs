#!/usr/local/bin/python

import time
import sys
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
from sklearn.cross_validation import train_test_split, KFold
from sklearn.ensemble import RandomForestRegressor

nrows=10000

def ReadData(path,name):
    onepath = path+"{0}_encoded_1.csv".format(name)
    twopath = path+"{0}_encoded_2.csv".format(name)
    skpath = path+"{0}_num_sk_rescaled.csv".format(name)
    paths = [onepath,twopath,skpath]
    dts = ["int16","int16","float32"]
    
    df = pd.DataFrame()
    for path,dt in zip(paths,dts):
        tmp = pd.read_csv(path,dtype=dt,nrows=nrows)
        df = pd.concat([df,tmp],axis=1)
        del tmp
    return df

path = "/home/guoli/work/learn_all/11282016_stack/000_data/"
df = ReadData(path,"train")
df["loss"] = np.log(pd.read_csv(path+"train_loss.csv",nrows=nrows).loss+200)

target = "loss"
features = list(df.columns.values)
features.remove(target)

kf = KFold(len(df.index),5)
scores = []
for ne in [100,200,300]:
    for mf in [0.2,0.4,0.6]:
        for md in [4,8,12]:
            for ms in [1,2,4]:
                for train_index, test_index in kf:
                    start = time.time()
                    train, valid = df.iloc[train_index,:], df.iloc[test_index,:]
                    rf = RandomForestRegressor(n_estimators=ne,
                                               max_features=mf,
                                               max_depth=md,
                                               min_samples_leaf=ms,
                                               n_jobs=4)
                    rf.fit(train[features],train[target])
                
                    Y = rf.predict(valid[features])
                    score = mean_absolute_error(np.exp(Y),np.exp(valid[target]))
                    scores.append(score)
                #    print score, time.time()-start
                print ne, mf, md, ms, np.mean(scores), np.std(scores)
