from gensim.models import Word2Vec

model = Word2Vec.load("data/genes/ProkariotesORFskipgram10features_1context_0downsampling")

print(model.similarity("atg", "tag"))
print(model.similarity("atg", "ccg"))
print(model.similarity("atg", "aag"))
print(model.similarity("atg", "aaa"))
print(model.similarity("tag", "taa"))
print(model.similarity("tag", "tga"))
print(model.similarity("ttt", "ggg"))
print(model.similarity("ttt", "gtc"))

codons = ["aaa", "aat", "aac", "aag",
          "ata", "att", "atc", "atg",
          "aca", "act", "acc", "acg",
          "aga", "agt", "agc", "agg",
          "taa", "tat", "tac", "tag",
          "tta", "ttt", "ttc", "ttg",
          "tca", "tct", "tcc", "tcg",
          "tga", "tgt", "tgc", "tgg",
          "caa", "cat", "cac", "cag",
          "cta", "ctt", "ctc", "ctg",
          "cca", "cct", "ccc", "ccg",
          "cga", "cgt", "cgc", "cgg",
          "gaa", "gat", "gac", "gag",
          "gta", "gtt", "gtc", "gtg",
          "gca", "gct", "gcc", "gcg",
          "gga", "ggt", "ggc", "ggg"]

for i in codons:
    for j in codons:
        print (i, " ", j, " ", model.similarity(i, j))


print ("\n\n\n")

for i in codons:
    print (i, " ", model.most_similar(i, topn=5))