from AverageVectors import average_vectors
from BagOfCentroids import bag_of_centroids
from analyse_results import analyse_results


def get_features_count(model_name):
    tmp = model_name.split('_')
    for t in tmp:
        if t.count('features') > 0:
            return int(t.replace('features', ''))

res = open("results.txt", 'a')

# Models:
models = ["data/genes/skip-gram_ns_softmax_300features_10context_Eu",       # 0  eukaryotes + skip-gram
          "data/genes/cbow_ns_softmax_300features_10context_Eu",            # 1  eukaryotes + CBOW
          "data/genes/skip-gram_ns_softmax_300features_10context_PurePro",  # 2  pure prokaryotes + skip-gram
          "data/genes/cbow_ns_softmax_300features_10context_PurePro",       # 3  pure prokaryotes + CBOW
          "data/genes/skip-gram_ns_softmax_300features_10context_Full",     # 4  full + skip-gram
          "data/genes/cbow_ns_softmax_300features_10context_Full",          # 5  full + CBOW
          "data/genes/skip-gram_ns_softmax_300features_10context_Mixed",    # 6  mixed + skip-gram
          "data/genes/cbow_ns_softmax_300features_10context_Mixed",         # 7  mixed + CBOW
          "data/genes/skip-gram_neg_300features_10context_Pro",             # 8  prokaryotes + skip-gram
          "data/genes/cbow_neg_300features_10context_Pro",                  # 9  prokaryotes + CBOW
          "data/genes/skip-gram_neg_300features_10context_Mouse",           # 10  mouse + skip-gram
          "data/genes/cbow_neg_300features_10context_Mouse",                # 11  mouse + CBOW
          "data/genes/skip-gram_neg_soft_300features_10context_Full",       # 12  full + negative + softmax
          "data/genes/skip-gram_soft_300features_10context_Full",           # 13  full + softmax
          "data/genes/skip-gram_neg_soft_10features_10context_Mouse",       # 14  mouse + 10 features
          "data/genes/skip-gram_neg_soft_50features_10context_Mouse",       # 15  mouse + 50 features
          "data/genes/skip-gram_neg_soft_100features_10context_Mouse",      # 16  mouse + 100 features
          "data/genes/skip-gram_neg_soft_300features_10context_Mouse",      # 17  mouse + 300 features
          "data/genes/skip-gram_neg_soft_500features_10context_Mouse",      # 18  mouse + 500 features
          "data/genes/skip-gram_neg_soft_1000features_10context_Mouse",     # 19  mouse + 1000 features
          "data/genes/skip-gram_neg_soft_50features_1context_Mouse",        # 20  mouse + 1 context
          "data/genes/skip-gram_neg_soft_50features_5context_Mouse",        # 21  mouse + 5 context
          "data/genes/skip-gram_neg_soft_50features_20context_Mouse",       # 22  mouse + 20 context
          "data/genes/skip-gram_neg_soft_50features_50context_Mouse",       # 23  mouse + 50 context
          "data/genes/skip-gram_neg_soft_50features_100context_Mouse",      # 24  mouse + 100 context + 50 features (!!!)
          "data/genes/skip-gram_neg_soft_50features_1context_Pro",          # 25  prokaryotes + 1 context
          "data/genes/skip-gram_neg_soft_50features_10context_Pro",         # 26  prokaryotes + 10 context
          "data/genes/skip-gram_neg_soft_50features_100context_Pro",        # 27  prokaryotes + 100 context + 50 features (!!!)
          "data/genes/skip-gram_neg_soft_50features_100context_Mixed",      # 28  mixed + 100 context + 50 features (!!!)
          "data/genes/cbow_neg_soft_50features_100context_Mixed",           # 29  CBOW mixed + 100 context + 50 features
          "data/genes/cbow_neg_soft_50features_100context_Pro",             # 30  CBOW prokaryotes + 100 context + 50 features
          "data/genes/cbow_neg_soft_50features_100context_Mouse",           # 31  CBOW mouse + 100 context + 50 features
          "data/genes/skip-gram_neg_soft_10features_100context_Pro",        # 32  prokaryotes + 10 features
          "data/genes/skip-gram_neg_soft_100features_100context_Pro",       # 33  prokaryotes + 100 features
          "data/genes/skip-gram_neg_soft_300features_100context_Pro",       # 34  prokaryotes + 300 features
          "data/genes/skip-gram_neg_soft_500features_100context_Pro",       # 35  prokaryotes + 500 features
          "data/genes/skip-gram_neg_soft_1000features_100context_Pro",      # 36  prokaryotes + 1000 feature
          "data/genes/skip-gram_neg_soft_50features_1context_Pro",          # 37  prokaryotes + 1 context
          "data/genes/skip-gram_neg_soft_50features_5context_Pro",          # 38  prokaryotes + 5 context
          "data/genes/skip-gram_neg_soft_50features_20context_Pro",         # 39  prokaryotes + 20 context
          "data/genes/skip-gram_neg_soft_50features_50context_Pro",         # 40  prokaryotes + 50 context
          "data/genes/skip-gram_neg_soft_50features_50context_Mixed",       # 41  mixed + 50 context
          "data/genes/skip-gram_neg_soft_50features_20context_Mixed",       # 42  mixed + 20 context
          "data/genes/skip-gram_neg_soft_50features_5context_Mixed",        # 43  mixed + 5 context
          "data/genes/skip-gram_neg_soft_50features_1context_Mixed",        # 44  mixed + 1 context
          "data/genes/skip-gram_neg_soft_10features_100context_Mixed",      # 45  mixed + 10 features
          "data/genes/skip-gram_neg_soft_100features_100context_Mixed",     # 46  mixed + 100 features
          "data/genes/skip-gram_neg_soft_300features_100context_Mixed",     # 47  mixed + 300 features
          "data/genes/skip-gram_neg_soft_500features_100context_Mixed",     # 48  mixed + 500 features
          "data/genes/skip-gram_neg_soft_1000features_100context_Mixed",    # 49  mixed + 1000 features
          "data/genes/skip-gram_neg_soft_1features_100context_Mixed",       # 50  mixed + 1 feature
          "data/genes/skip-gram_neg_soft_1features_100context_Pro",         # 51  prokaryotes + 1 feature
          "data/genes/skip-gram_neg_soft_1features_100context_Mouse"]       # 52  mouse + 1 feature

# Bases:
bases = {"full": "data/genes/full/",
         "mixed": "data/genes/pro+eu (mixed)/",
         "pure_pro": "data/genes/pure_pro(+pro_nc)/",
         "prokaryotes": "data/genes/prokaryotes/",
         "eukaryotes": "data/genes/eu(human+mouse+rat)/",
         "mouse": "data/genes/mouse_and_rat/",
         "human": "data/genes/human/"}

# Methods:
bag = "data/genes/BagOfCentroids.csv"
vec = "data/genes/Genes_AverageVectors.csv"

# Parameters:
n = 7  # number of repetitions
model = models[52]
base = bases["mouse"]
method = bag

total = 0
true_res = 0
false_res = 0
geneCalledNC = 0
ncCalledGene = 0

# Start with given parameters N times
log = "Starting " + str(n) + " times  with model " + model + " on base " + base + " by method " + method
print log
res.write(log + "\n")
for i in range(0, n):
    print "Step " + str(i)
    if method == bag:
        bag_of_centroids(model, base)
    elif method == vec:
        average_vectors(model, base, get_features_count(model))
    else:
        break
    tmp_res = analyse_results(method)
    total += tmp_res[0]
    true_res += tmp_res[1]
    false_res += tmp_res[2]
    ncCalledGene += tmp_res[3]
    geneCalledNC += tmp_res[4]

log = 'Total analysed seqs  = ' + str(total)
print log
res.write(log + "\n")
log = 'Right results = ' + str(true_res) + '(% of total = ' + str(float(true_res) / float(total) * 100) + ')'
print log
res.write(log + "\n")
log = 'Wrong results = ' + str(false_res) + '(% of total = ' + str(float(false_res) / float(total) * 100) + ')'
print log
res.write(log + "\n")
log = 'False-positive results  = ' + str(ncCalledGene) + '(% of all wrong = ' + \
                            str(float(ncCalledGene) / float(false_res) * 100) + ')'
print log
res.write(log + "\n")
log = 'False-negative results = ' + str(geneCalledNC) + '(% of all wrong = ' + \
                            str(float(geneCalledNC) / float(false_res) * 100) + ')'
print log
res.write(log + "\n")
res.write('\n ----------------------------------------\n\n')

res.close()