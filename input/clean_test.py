#!/usr/local/bin/python
import string
import numpy as np
from collections import Counter
import itertools
import json

f = open('raw/test.csv','r')
lines = f.readlines()
f.close()

f = open("test.csv","w")
for line in lines:
    line = line.replace('\n','\r')
    line = line.replace('"\r','"\n')
    line = line.replace('\r',"")
    line = line.replace('\\','|')
    line = line.replace(',',";")
    line = line.replace('";','",')
    line = line.replace('"",','"";')
    line = line.replace('""";','""",')
    line = line.replace('",",','","')
    line = line.replace(',"";',',"",')
    line = line.replace(';',',',1)
    line = line.replace(',"";',',"",')
    line = line.replace(',",',',"')
    line = line.replace('],','];')
    line = line.decode('unicode_escape').encode('ascii','ignore')
    f.write(line)
f.close()

f = open("test.csv","r")
lines = f.readlines()
f.close()
for line in lines:
    if line.count(',') != 2:
        print line.count(','), line
        print line.split(',')
