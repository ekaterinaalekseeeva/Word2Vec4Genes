import random


# in_file = open('genesTrainData_codones.tsv')
in_file = open('genesUnlabeledTrainData_codones.tsv')
# in_file = open('genesTestData_codones.tsv')
# out = open('genesTestDataShuffle.tsv', 'w+')
out = open('genesUnlabeledTrainDataShuffle.tsv', 'w+')
# out = open('genesTrainDataShuffle.tsv', 'w+')

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
