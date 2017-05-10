def prepare_train_data():
    in_file = open('tmp.tsv')
    out = open('genesUnlabeledTrainData.tsv', 'w+')
    # out = open('data/genes/human_export.tsv', 'w+')
    # out = open('data/genes/nrna.tsv', 'w')
    # tmp = open('data/genes/tmp.tsv', 'r+')

    lines = []
    for line in in_file.readlines():
        lines.append(line)

    for i in range(0, len(lines) - 1):
        # print lines[i + 1]
        # print lines[i + 1].startswith('>')
        if lines[i + 1].startswith('Sequence unavailable') or lines[i].startswith('Sequence unavailable'):
            l = ''
        else:
            # l = lines[i]
            if not lines[i + 1].startswith('>'):
                l = lines[i].replace('\n', '')
            else:
                l = lines[i]
            if lines[i].startswith('>'):
                if len(lines[i]) > 40:
                    if lines[i].startswith('>ENS'):
                        l = l[:18]
                        l += ';'
                    else:
                        l = l[:9]
                        l += ';'
                else:
                    l += ';'
            # elif not lines[i].startswith('id'):
            #     l = ''
            #     if len(lines[i]) % 3 == 0:
            #         tmp = wrap(l, 3)
            #     if len(lines[i]) % 3 == 1:
            #         l+=l[:1]
            #         tmp = wrap(l, 3)
            #     if len(lines[i]) % 3 == 2:
            #         tmp = wrap(l, 3)
            #     tmp2 = ''
            #     for t in tmp:
            #         tmp2 += t + ' '
            #     l += tmp2
            # if not lines[i + 1].startswith('>'):
            #     l = l.replace('\n', ' ')
            # else:
            #     l += '\n'
        out.write(l)

    out.close()
    in_file.close()

prepare_train_data()