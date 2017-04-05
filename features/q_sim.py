#!/usr/bin/env python
# This code generates a one-column csv file with 
# column name 'q_sim' meaning the similarity between two questions
# Xin Kou
# last modified: 2017-04-05

from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import numpy as np
from scipy import spatial


"""word2vec model pretrained by GoogleNews 
To reload this model, please first download GoogleNews-vectors-negative300.bin from 
 https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit"""
model = KeyedVectors.load_word2vec_format('../../Downloads/GoogleNews-vectors-negative300.bin', binary=True)

def q_vec(question):
    """convert the question to a vector by averaging the vectors of
        all words contained in the question
        each word vector is a 300 dimentional vector
        return a np.array    
        parameters
        ----------
        question: a list of words"""

    vec=np.zeros(300)
    if len(question): # nonempty question
        for w in question:
            if w in model:            
                vec+=model[w]
        vec=vec/len(question)
    return vec

def q_sim(q1,q2):
    """cosine similarity between two questions q1 and q2
    	return a number between 0 and 1

        parameters
        ----------
        q1,q2: lists of words"""
    q1_vec=q_vec(q1)
    q2_vec=q_vec(q2)
    if q1_vec.sum() and q2_vec.sum(): #nonzero vectos
        sim = 1-spatial.distance.cosine(q1_vec,q2_vec)
    else:
    	# if any vector is zero, we let the similarity be zero
        sim = 0
    return sim

def xGenerate(col,in_name,out_name):
	""" generate feature 

		parameters
        ----------
		col: feature name
		in_name: name of the cleaned data csv file, containing two columns 
				'question1' and 'question2'
		out_name: name of the feature csv file, with column name col 
        """
    f = open(in_name,"r")
    lines = f.readlines()
    f.close()

    f = open(out_name,"w")
    f.write(col+"\n")
    for line in lines[1:]:
        items = line[:-1].split(",")
        q1 = items[0].split() # list of words
        q2 = items[1].split() # list of words
       	f.write("{0:.4f}\n".format(q_sim(q1,q2)))



in_name = "stops_train_clean.csv" #without stop word and no stemming
out_name = "q_sim_no_stop.csv"
xGenerate("q_sim",in_name,out_name)