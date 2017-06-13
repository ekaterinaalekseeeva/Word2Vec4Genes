import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk.data
import logging


def sequence_to_wordlist(sequence):
    # Function to convert a document to a sequence of words,
    # optionally removing stop words.  Returns a list of words.
    #
    # 1. Remove HTML
    sequence_text = BeautifulSoup(sequence, features='lxml').get_text()
    #
    # 2. Remove non-letters
    sequence_text = re.sub("[^a-zA-Z]", " ", sequence_text)
    #
    # 3. Convert words to lower case and split them
    words = sequence_text.lower().split()
    #
    # 4. Optionally remove stop words (false by default)
    # if remove_stopwords:
    #     stops = set(stopwords.words("english"))
    #     words = [w for w in words if not w in stops]
    #
    # 5. Return a list of words
    return (words)


# Define a function to split a review into parsed sentences
def sequence_to_sentences(sequence, tokenizer):
    # Function to split a review into parsed sentences. Returns a
    # list of sentences, where each sentence is a list of words
    #
    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(sequence.strip().decode('utf-8'))
    #
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call sequence_to_wordlist to get a list of words
            sentences.append(sequence_to_wordlist(raw_sentence))
    #
    # Return the list of sentences (each sentence is a list of words,
    # so this returns a list of lists
    return sentences


# base = "full/"
# base = "pro+eu (mixed)/"
# base = "prokaryotes/"
# base = "pure_pro(+pro_nc)/"
base = "pro/"
# base =  "mouse_and_rat/"
# base = "eu(human+mouse+rat)/"
# base =  "human/"

# Read data from files
train = pd.read_csv(base + "genesTrainDataShuffle.tsv", header=0,
                    delimiter=";", quoting=3)
test = pd.read_csv(base + "genesTestDataShuffle.tsv", header=0, delimiter=";", quoting=3)
# unlabeled_train = pd.read_csv("genesUnlabeledTrainDataShuffle.tsv", header=0,
#                               delimiter=";", quoting=3)

# Verify the number of reviews that were read (100,000 in total)
# print "Read %d labeled train reviews, %d labeled test reviews, " \
#       "and %d unlabeled reviews\n" % (train["sequence"].size,
#                                       test["sequence"].size, unlabeled_train["sequence"].size)

print "Read %d labeled train reviews and %d labeled test reviews, " % (train["sequence"].size,
                                                                       test["sequence"].size)

# Download the punkt tokenizer for sentence splitting
# nltk.download()

# Load the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

sentences = []  # Initialize an empty list of sentences

print "Parsing sentences from training set"
for sequence in train["sequence"]:
    # print train["isgene"]
    # print sequence
    sentences += sequence_to_sentences(sequence, tokenizer)
    # sentences += sequence_to_sentences(sequence)


# Import the built-in logging module and configure it so that Word2Vec
# creates nice output messages
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                    level=logging.INFO)


# Set values for various parameters
skip_gram = 1  # skip-gram = 1, cbow = 0
negative_sampling = 1
hie_softmax = 1
num_features = 300  # Word vector dimensionality
context = 100  # Context window size
downsampling = 0  # Downsample setting for frequent words

min_word_count = 1  # Minimum word count
num_workers = 4  # Number of threads to run in parallel

# Initialize and train the model (this will take some time)
from gensim.models import word2vec

print "Training model..."
model = word2vec.Word2Vec(sentences, sg=skip_gram, hs=hie_softmax, negative=negative_sampling, \
                          workers=num_workers, \
                          size=num_features, min_count=min_word_count, \
                          window=context, sample=downsampling)

# If you don't plan to train the model any further, calling
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)

# It can be helpful to create a meaningful model name and
# save the model for later use. You can load it later using Word2Vec.load()
if skip_gram == 1:
    type = "skip-gram"
else:
    type = "cbow"
func = ''
if negative_sampling == 1 and hie_softmax == 0:
    func = "neg"
elif hie_softmax == 1 and negative_sampling == 0:
    func = "soft"
elif negative_sampling == 1 and hie_softmax == 1:
    func = "neg_soft"

b = ''
if base == "full/":
    b = "Full"
elif base == "pro+eu (mixed)/":
    b = "Mixed"
elif base == "prokaryotes/":
    b = "Pro"
elif base == "pro/":
    b = "TruePro"
elif base == "pure_pro(+pro_nc)/":
    b = "PurePro"
elif base == "mouse_and_rat/":
    b = "Mouse"
elif base == "eu(human+mouse+rat)/":
    b = "Eu"
elif base == "human/":
    b = "Human"

model_name = type + '_' + func + '_' + str(num_features) + 'features_' + str(context) + 'context_' + b
print model_name
# model_name = "skip-gram_ns_softmax_300features_10context_Pro"
model.save(model_name)
