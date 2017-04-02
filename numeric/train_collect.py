#!/Users/guoli/anaconda2/bin/python
import pandas as pd
import numpy as np

fnames = ["../features/001_word_count/001_word_count/train_wordcount.csv",
          "../features/001_word_count/002_word_count_tfidf/train_wordcount_tfidf.csv",
          "../features/002_norm_dist/001_norm_dist/train_normdist.csv",
          "../features/001_word_count/003_word_count_nostem/train_wordcount_nostem.csv",
          "../features/004_question_kind/train_WhatDiffCount.csv"
          ]

df = pd.read_csv("../input/train_clean.csv",usecols=["is_duplicate"])
for fname in fnames:
    df1 = pd.read_csv(fname)
    for col in df1.columns.values:
        df[col] = df1[col]
    
df.to_csv("train_numeric.csv",index=False)

