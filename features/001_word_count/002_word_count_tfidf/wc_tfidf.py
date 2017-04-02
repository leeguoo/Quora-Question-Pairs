#!/Users/guoli/anaconda2/bin/python
import json
#fname = "idf_allwords_stem_stops.json"
fname = "idf_allwords_stem_stops.json"
f = open(fname,"r")
data = json.load(f)

def idf_shared_word_count(s1,s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    both = set1|set2
    shared = set1&set2
    if len(shared)==0:
        return 0
    else:
        LL = 0
        for k in both:
            LL += data[k]
        L = 0
        for k in shared:
            L += data[k] 
        return L/LL
      
def xGenerate(col, in_name,out_name):
    f = open(in_name,"r")
    lines = f.readlines()
    f.close()

    f = open(out_name,"w")
    f.write(col+"\n")
    for line in lines[1:]:
        items = line[:-1].split(",")
        f.write("{0:.5E}\n".format(idf_shared_word_count(items[0],items[1])))

in_name = "../../../input/stem_stops_train_clean.csv"
out_name = "train_wordcount_tfidf.csv"
xGenerate("WC_tfidf",in_name,out_name)
