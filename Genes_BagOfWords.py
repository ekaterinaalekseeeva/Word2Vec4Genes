import os
from time import sleep

import nltk
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from KaggleWord2VecUtility import KaggleWord2VecUtility
import pandas as pd
import numpy as np


def sequence_to_codons(review):
    # Function to convert a document to a sequence of words,
    # optionally removing stop words.  Returns a list of words.
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(review, features='lxml').get_text()  # .decode("utf8")
    #
    # 2. Remove non-letters
    review_text = nltk.re.sub("[^a-zA-Z]", " ", review_text)
    #
    # 3. Convert words to lower case and split them
    words = review_text.lower().split()
    # print words
    # sleep(10)
    #
    # 5. Return a list of words
    return words


def analyse():
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data/genes', 'genesTrainDataShuffle.tsv'), header=0, \
                        delimiter=";", quoting=3)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data/genes', 'genesTestDataShuffle.tsv'), header=0,
                       delimiter=";", \
                       quoting=3)

    print 'The first sequence is:'
    print train  # ["sequence"][2]
    print test

    #  Initialize an empty list to hold the clean reviews
    clean_train_sequences = []

    # Loop over each review; create an index i that goes from 0 to the length
    # of the movie review list

    print "Cleaning and parsing the training set movie reviews...\n"
    for i in xrange(0, len(train["sequence"])):
        clean_train_sequences.append(" ".join(sequence_to_codons(train["sequence"][i])))

    print "Creating the bag of words...\n"  # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer="word", \
                                 tokenizer=None, \
                                 preprocessor=None, \
                                 stop_words=None, \
                                 max_features=10000)

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of
    # strings.
    print clean_train_sequences
    train_data_features = vectorizer.fit_transform(clean_train_sequences)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    train_data_features = train_data_features.toarray()

    # ******* Train a random forest using the bag of words
    #
    print "Training the random forest (this may take a while)..."

    # Initialize a Random Forest classifier with 100 trees
    forest = RandomForestClassifier(n_estimators=100)

    # Fit the forest to the training set, using the bag of words as
    # features and the sentiment labels as the response variable
    #
    # This may take a few minutes to run
    forest = forest.fit(train_data_features, train["isgene"])

    # Create an empty list and append the clean reviews one by one
    clean_test_reviews = []

    print "Cleaning and parsing the test set movie reviews...\n"
    for i in xrange(0, len(test["sequence"])):
        clean_test_reviews.append(" ".join(sequence_to_codons(test["sequence"][i])))
        # clean_test_reviews.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(test["sequence"][i], True)))

    # Get a bag of words for the test set, and convert to a numpy array
    test_data_features = vectorizer.transform(clean_test_reviews)
    test_data_features = test_data_features.toarray()

    # Use the random forest to make sentiment label predictions
    print "Predicting test labels...\n"
    result = forest.predict(test_data_features)

    # Copy the results to a pandas dataframe with an "id" column and
    # a "sentiment" column
    output = pd.DataFrame(data={"id": test["id"], "isgene": result})

    # Use pandas to write the comma-separated output file
    output.to_csv(os.path.join(os.path.dirname(__file__), 'data/genes', 'Bag_of_Words_model.csv'), index=False,
                  quoting=3)
    print "Wrote results to Bag_of_Words_model.csv"

if __name__ == '__main__':

    analyse()