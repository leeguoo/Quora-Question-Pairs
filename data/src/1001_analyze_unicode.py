#!/home/guoli/anaconda2/bin/python
import string
import chardet
import re
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
import json

f = open("nonunicode","r")
lines = f.readlines()
f.close()

items = [line.split()[0] for line in lines]
item_els = []
for item1 in items:
    for item2 in items:
        if item1 != item2 and item1 in item2:
            item_els.append(item1)

for el in set(item_els):
    print el
