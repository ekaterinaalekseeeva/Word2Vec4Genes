#!/usr/bin/python

# encoding=utf8

import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import nltk.data


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



# Read data from files
train = pd.read_csv("genesTrainDataShuffle.tsv", header=0,
                    delimiter=";", quoting=3)
test = pd.read_csv("genesTestDataShuffle.tsv", header=0, delimiter=";", quoting=3)
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
    sentences += sequence_to_sentences(sequence, tokenizer)
    # sentences += sequence_to_sentences(sequence)

# print "Parsing sentences from unlabeled set"
# for sequence in unlabeled_train["sequence"]:
#     sentences += sequence_to_sentences(sequence, tokenizer)
    # sentences += sequence_to_sentences(sequence)

# Import the built-in logging module and configure it so that Word2Vec
# creates nice output messages
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                    level=logging.INFO)

# Set values for various parameters
num_features = 10  # Word vector dimensionality
min_word_count = 1  # Minimum word count
num_workers = 4  # Number of threads to run in parallel
context = 1  # Context window size
downsampling = 0  # Downsample setting for frequent words

# Initialize and train the model (this will take some time)
from gensim.models import word2vec

print "Training model..."
model = word2vec.Word2Vec(sentences, sg=1, workers=num_workers, \
                          size=num_features, min_count=min_word_count, \
                          window=context, sample=downsampling)

# If you don't plan to train the model any further, calling
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)

# It can be helpful to create a meaningful model name and
# save the model for later use. You can load it later using Word2Vec.load()
model_name = "ORFskipgram10features_1context_0downsampling"
model.save(model_name)
