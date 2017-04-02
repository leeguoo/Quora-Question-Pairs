#!/usr/local/bin/python
import string
import numpy as np
from collections import Counter
import itertools
import json

f = open('raw/train.csv','r')
lines = f.readlines()
f.close()

f = open("train.csv","w")
for line in lines:
    line = line.replace('\n','')
    line = line.replace('\r','\n')
    line = line.replace('\\','|')
    line = line.replace(',',";")
    line = line.replace('";','",')
    line = line.replace('"",','"";')
    line = line.replace('""";','""",')
    line = line.replace('",",','","')
    line = line.replace(',"";',',"",')
    line = line.decode('unicode_escape').encode('ascii','ignore')
    f.write(line)
f.close()

f = open("train.csv","r")
lines = f.readlines()
f.close()
for line in lines:
    if line.count(',') != 5:
        print line.count(','), line
