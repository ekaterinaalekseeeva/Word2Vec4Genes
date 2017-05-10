def prepare_test_data():
    in_file = open('testtmp.tsv')
    out = open('genesTestData.tsv', 'w+')
    # out = open('data/genes/nrna_test.tsv', 'w+')
    # tmp = open('data/genes/tmp.tsv', 'r+')

    lines = []
    for line in in_file.readlines():
        lines.append(line)

    for i in range(0, len(lines) - 2):
        # print lines[i + 1]
        # print lines[i + 1].startswith('>')
        if lines[i + 1].startswith('Sequence unavailable') or lines[i].startswith('Sequence unavailable'):
            l = ''
        else:
            if not lines[i + 1].startswith('>'):
                l = lines[i].replace('\n', '')
            else:
                l = lines[i]
            if lines[i].startswith('>'):
                if lines[i].startswith('>ENS'):
                    l = l[:18]
                    # l += ';'
                else:
                    l = l[:9]
                    # l += ';'
                l += ';'
        out.write(l)

    out.close()
    in_file.close()

prepare_test_data()