from textwrap import wrap


def wrap_codones (in_file, out):
    # lines = []
    first_line = ''
    i = 0
    for line in in_file.readlines():
        if i == 0:
            first_line = line
            out.write(first_line)
        else:
            if i % 100 == 0:
                print i
            index = line.rindex(';')+1
            start = line[:index]#.strip()
            end = line[index:].rstrip()
            end = end.replace('N', '')
            # end = end.rstrip()
            l = ''
            tmp = []

            # If sequence is not multiples of three, provide 3 variants of ORF
            if len(end) % 3 != 0:
                # Open reading frame 1
                tmp = wrap(end, 3)
                tmp2 = ''
                for t in tmp:
                    # print t
                    if len(t) == 3:
                        tmp2 += t + ' '
                if tmp2 != '':
                    out.write("ORF1" +start + tmp2 + '\n')

                # Open reading frame 2
                tmp = wrap(end[1:], 3)
                tmp2 = ''
                for t in tmp:
                    # print t
                    if len(t) == 3:
                        tmp2 += t + ' '
                if tmp2 != '':
                    out.write("ORF2" + start + tmp2 + '\n')

                #Open reading frame 3
                tmp = wrap(end[2:], 3)
                tmp2 = ''
                for t in tmp:
                    # print t
                    if len(t) == 3:
                        tmp2 += t + ' '
                if tmp2 != '':
                    out.write("ORF3" + start + tmp2 + '\n')
            # For those that are multiples of three just divide it to codons
            else:
                # if len(end) % 3 == 0:
                    # print '0'
                tmp = wrap(end, 3)
                # if len(end) % 3 == 1:
                #     print str(i) + ' 1'
                #     l += end[:1] + ' '
                #     tmp = wrap(end[1:], 3)
                # if len(end) % 3 == 2:
                #     print str(i) + '2'
                #     l += end[:2] + ' '
                #     tmp = wrap(end[2:], 3)
                tmp2 = ''
                for t in tmp:
                    # print t
                    tmp2 += t + ' '
                l += tmp2
                out.write(start + l + '\n')
        i += 1



# in_file = open('traintmp.tsv')
# in_file = open('testtmp.tsv')
# in_file = open('genesTrainData.tsv')
# out = open('genesTrainData_codones.tsv', 'w')
# out.close()
# out = open('genesTrainData_codones.tsv', 'a')
# in_file = open('genesTestData.tsv')
# out = open('genesTestData_codones.tsv', 'w')
# out.close()
# out = open('genesTestData_codones.tsv', 'a')
# in_file = open('genesUnlabeledTrainData.tsv')
# out = open('genesUnlabeledTrainData_codones.tsv', 'w')
# out.close()
# out = open('genesUnlabeledTrainData_codones.tsv', 'a')
# wrap_codones(in_file, out)

dir = ["full",
       "pro+eu (mixed)",
       "prokaryotes",
       # "pure_pro(+pro_nc)",
       "mouse_and_rat",
       # "eu(human+mouse+rat)",
       "human"]

type = ["Train", "Test"]

for d in dir:
    for j in type:
        print d + ' ' + j
        in_file = open(d+'/genes'+j+'Data_.tsv', 'r')
        out = open(d+'/genes'+j+'Data_codones_.tsv', 'w')

        wrap_codones(in_file, out)

        in_file.close()
        out.close()

# lines = []
# first_line = ''
# i = 0
# for line in in_file.readlines():
#     if i == 0:
#         first_line = line
#     else:
#         lines.append(line)
#     i += 1
#
# result = []
# lineNumber = 0
# for i in lines:
#     if lineNumber % 100 == 0:
#         print lineNumber
#     index = i.rindex(';')
#     start = i[:index]
#     end = i[index:].rstrip()
#     l = ''
#     tmp=[]
#     if len(end) % 3 == 0:
#         # print '0'
#         tmp = wrap(end, 3)
#     if len(end) % 3 == 1:
#         # print '1'
#         l += end[:1] + ' '
#         tmp = wrap(end[1:], 3)
#     if len(end) % 3 == 2:
#         # print '2'
#         l += end[:2] + ' '
#         tmp = wrap(end[2:], 3)
#     tmp2 = ''
#     for t in tmp:
#         # print t
#         tmp2 += t + ' '
#     l += tmp2
#     result.append(start+l+'\n')
#     lineNumber += 1
#
# out.write(first_line)
# for i in result:
#     out.write(i)
#
# in_file.close()
# out.close()