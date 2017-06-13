# in_file = open('data/genes/BagOfCentroids.csv')

bases = {"full": "data/genes/full/",
         "mixed": "data/genes/pro+eu (mixed)/",
         "pure_pro": "data/genes/pure_pro(+pro_nc)/",
         "prokaryotes": "data/genes/prokaryotes/",
         "pro": "data/genes/pro/",
         "eukaryotes": "data/genes/eu(human+mouse+rat)/",
         "mouse": "data/genes/mouse_and_rat/",
         "human": "data/genes/human/"}
base = bases["pure_pro"]
# type = "genesTrainDataShuffle.tsv"
type  = "genesTestDataShuffle.tsv"
# type  = "train.txt"
in_file = open(base + type)
out = open('data/genes/count_ids.txt', 'a')

out.write(base + ' ' + type + '\n\n')

ids = {">ENSG": 0,
       ">ENSMUSG": 0,
       ">ENSRNOG": 0,
       ">KMK": 0,
       ">ADH": 0,
       ">ADI": 0,
       ">AAT": 0,
       ">AAW": 0,
       ">EEC": 0,
       ">AKF": 0,
       ">GAK": 0,
       ">AFS": 0,
       ">EEG": 0,
       ">CDNA": 0,
       ">ENST": 0,
       ">ENSMUST": 0,
       ">NCRNA": 0}

for line in in_file.readlines():
    for n in ids.keys():
        if line.count(n) > 0:
            ids[n] += 1
            break

sum = 0
for i in ids:
        print str(i) + ': ' + str(ids[i])
        out.write(str(i) + ': ' + str(ids[i]) + '\n')
        sum += ids[i]

print sum

out.write('\n ----------------------------------------\n\n')