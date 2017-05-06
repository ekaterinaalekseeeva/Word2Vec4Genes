from datetime import datetime

# in_file = open('Bag_of_Words_model.csv')
in_file = open('BagOfCentroids.csv')
# in_file = open('Word2Vec_AverageVectors.csv')
out = open ('analyse_results.txt', 'a')

true_res = 0
false_res = 0
geneCalledNC = 0
ncCalledGene = 0
total = 0
for line in in_file.readlines():
    if line.count('>ENSG') > 0:
        if line.count(',1') > 0:
            true_res += 1
        else:
            false_res += 1
            geneCalledNC += 1
    else:
        if line.count(',1') > 0:
            false_res += 1
            ncCalledGene += 1
        else:
            true_res += 1
    total += 1


print in_file.name
out.write(in_file.name + ' ' + str(datetime.now()) + "\n")
print 'Total analysed seqs  = ' + str(total)
out.write( 'Total analysed seqs  = ' + str(total)+'\n')
print 'Right results = ' + str(true_res) + '(% of total = ' + str(float(true_res)/float(total) * 100) + ')'
out.write( 'Right results = ' + str(true_res) + '(% of total = ' + str(float(true_res)/float(total) * 100) + ')\n')
print 'Wrong results = ' + str(false_res) + '(% of total = ' + str(float(false_res)/float(total) * 100) + ')'
out.write( 'Wrong results = ' + str(false_res) + '(% of total = ' + str(float(false_res)/float(total) * 100) + ')\n')
print 'False-positive results  = ' + str(ncCalledGene) + '(% of all wrong = ' + str(float(ncCalledGene)/float(false_res) * 100) + ')'
out.write( 'False-positive results  = ' + str(ncCalledGene) + '(% of all wrong = ' + str(float(ncCalledGene)/float(false_res) * 100) + ')\n')
print 'False-negative results = ' + str(geneCalledNC) + '(% of all wrong = ' + str(float(geneCalledNC)/float(false_res) * 100) + ')'
out.write( 'False-negative results = ' + str(geneCalledNC) + '(% of all wrong = ' + str(float(geneCalledNC)/float(false_res) * 100) + ')\n')
out.write('\n ----------------------------------------\n\n')
