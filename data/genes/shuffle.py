import random


in_file = open('human/genesTrainData_codones_.tsv')
out = open('human/genesTrainDataShuffle.tsv', 'w+')
# # in_file = open('genesUnlabeledTrainData_codones.tsv')
# out = open('genesUnlabeledTrainDataShuffle.tsv', 'w+')
# in_file = open('human/genesTestData_codones_.tsv')
# out = open('human/genesTestDataShuffle.tsv', 'w+')


lines = []
first_line = ''
i = 0
for line in in_file.readlines():
    if i == 0:
        first_line = line
    else:
        lines.append(line)
    i += 1

random.shuffle(lines)

out.write(first_line)
for i in lines:
    out.write(i)

in_file.close()
out.close()
