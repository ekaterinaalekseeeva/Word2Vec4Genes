def split_file():
    in_file = open('data/genomes/'+str(n)+'.txt')
    desc_file = open('data/genomes/'+str(n)+'desc.txt', 'w')
    seq_file = open('data/genomes/'+str(n)+'seq.txt', 'w')
    flag = False
    for i in in_file.readlines():
        if i.count('//') == 0:
            if not flag:
                desc_file.write(i)
            else:
                seq_file.write(i)
            if i.count('ORIGIN') > 0:
                flag = True

    in_file.close()
    desc_file.close()
    seq_file.close()


def parse_desc():
    desc = open('data/genomes/'+str(n)+'desc.txt')
    coord = open('data/genomes/'+str(n)+'coord.txt', 'w')

    count = 0
    for line in desc.readlines():

        # print line.count('gene')
        if line.count('gene ') > 0:
            # print '11111111111111'
            # print line
            l = line.replace("complement", ' ')
            # print l
            t = l.replace('\t', ' ')
            l = t.replace('.', ' ')
            t = l.replace('\n', ' ')
            l = t.replace('(', ' ')
            t = l.replace(')', ' ')
            l = t
            # print l
            tmp = l.split(' ')
            # print tmp
            if tmp[17] != '' and tmp[19]!='':
                count += 1
                start = int(tmp[17])
                stop = int(tmp[19])
                print str(start) + " " + str(stop)
                coord.write(str(start) + " " + str(stop) + "\n")
            elif tmp[19] != '' and tmp[21]!='':
                count += 1
                start = int(tmp[19])
                stop = int(tmp[21])
                print str(start) + " " + str(stop)
                coord.write(str(start) + " " + str(stop) + " complement\n")

    coord.close()
    desc.close()


def parse_seq():
    seq = open('data/genomes/'+str(n)+'seq.txt')
    sequences = open('data/genomes/'+str(n)+"sequences.txt", 'w')
    for line in seq.readlines():
        l = line.split(' ')
        for i in l:
            flag = False
            for symbol in i:
                if '1234567890'.find(symbol) == -1:
                    flag = True
                    break
            if flag:
                sequences.write(i.replace('\n', ''))
    seq.close()
    sequences.close()


def complement(string):
    # print string
    tmp = []
    for i in string:
        if i == 'a':
            tmp.append('t')
        if i == 't':
            tmp.append('a')
        if i == 'c':
            tmp.append('g')
        if i == 'g':
            tmp.append('c')
    res = ''.join(tmp)
    return res[::-1]


def split_seq():
    coord = open('data/genomes/'+str(n)+'coord.txt',)
    sequences = open('data/genomes/'+str(n)+"sequences.txt")
    cdna_file = open('data/genomes/ready/'+str(n)+'cdna.txt', 'w')
    ncrna_file = open('data/genomes/ready/'+str(n)+'ncrna.txt', 'w')

    count_gene = 0
    count_not_gene = 0
    last = 0
    seq = sequences.readline()
    # print seq
    for i in coord.readlines():
        start = int(i.split(' ')[0])
        stop = int(i.split(' ')[1])
        # print start
        # print stop
        ncrna = seq[last:start-1]
        if len(ncrna) >= 3:
            ncrna_file.write('>NCRNA' + str(n) + '_' + str(count_not_gene) + ';' + ncrna + '\n')
            # ncrna_file.write('>NCRNA' + str(n) + '_' + str(count_not_gene) + ';0;' + ncrna + '\n')
            count_not_gene += 1
        if len(i.split(' ')) == 3:
            # print i.split(' ')[2]
            tmp = seq[start-1:stop]
            cdna = complement(tmp)
        else:
            cdna = seq[start-1:stop]
        cdna_file.write('>CDNA' + str(n) + '_'+ str(count_gene) + ';' + cdna + '\n')
        # cdna_file.write('>CDNA' + str(n) + '_'+ str(count_gene) + ';1;' + cdna + '\n')
        count_gene += 1
        last = stop


for n in range(3, 6):
    split_file()
    parse_desc()
    parse_seq()
    split_seq()