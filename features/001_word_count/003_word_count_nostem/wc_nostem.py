#!/Users/guoli/anaconda2/bin/python

def shared_word_count(s1,s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    L = len(set1|set2)
    if L == 0:
        return 0
    else:
        return 1.0*len(set1&set2)/L
      
def xGenerate(col,in_name,out_name):
    f = open(in_name,"r")
    lines = f.readlines()
    f.close()

    f = open(out_name,"w")
    f.write(col+"\n")
    for line in lines[1:]:
        items = line[:-1].split(",")
        f.write("{0:.5E}\n".format(shared_word_count(items[0],items[1])))

in_name = "../../../input/stops_train_clean.csv"
out_name = "train_wordcount_nostem.csv"
xGenerate("WC_nostem",in_name,out_name)
