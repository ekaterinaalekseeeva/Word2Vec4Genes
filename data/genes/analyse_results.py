from datetime import datetime

# in_file = open('Bag_of_Words_model.csv')
# in_file = open('BagOfCentroids.csv')
in_file = open('Genes_AverageVectors.csv')
out = open ('analyse_results.txt', 'a')
outres = open('res.csv', 'w+')

true_res = 0
false_res = 0
geneCalledNC = 0
ncCalledGene = 0
total = 0
i = 0
for line in in_file.readlines():
    if i != 0:  #just ignore the first line (title)
        if line.count('>ENST') > 0 or line.count('>ENSM') > 0:  # if it is not a gene
            if line.count(',0') > 0:  # and program said '0' -- not a gene
                true_res += 1
                outres.write(line[:-1] + ' true\n')  # then it is a right answer
            elif line.count(',1') > 0:
                false_res += 1
                geneCalledNC += 1
                outres.write(line[:-1] + ' false\n')  # else it's wrong
            else:
                outres.write(line + 'WTF???\n')  # just for sure that nothing's missed
        else:  # else (if it's a gene)
            if line.count(',0') > 0:  # and program said  '0' -- not a gene
                false_res += 1
                ncCalledGene += 1
                outres.write(line[:-1] + ' false\n')  # then it is wrong answer
            elif line.count(',1') > 0:
                true_res += 1
                outres.write(line[:-1] + ' true\n')  # else it's right
            else:
                outres.write(line + 'WTF???\n')  # just for sure that nothing's missed
        total += 1
    else:
        outres.write(line[:-1] + ' analyse\n')  # just write the first line without changes
    i += 1  # line counter


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
