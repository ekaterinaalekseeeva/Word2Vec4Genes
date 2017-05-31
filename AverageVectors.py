import pandas as pd
import numpy as np  # Make sure that numpy is imported
from gensim.models import Word2Vec
from sklearn.ensemble import RandomForestClassifier


# ****** Define functions to create average word vectors
def makeFeatureVec(words, model, num_features):
    # Function to average all of the word vectors in a given
    # paragraph
    #
    # Pre-initialize an empty numpy array (for speed)
    featureVec = np.zeros((num_features,),dtype="float32")
    #
    nwords = 0.
    #
    # Index2word is a list that contains the names of the words in
    # the model's vocabulary. Convert it to a set, for speed
    index2word_set = set(model.index2word)
    #
    # Loop over each word in the review and, if it is in the model's
    # vocabulary, add its feature vector to the total
    for word in words:
        if word in index2word_set:
            nwords = nwords + 1.
            featureVec = np.add(featureVec,model[word])
    #
    # Divide the result by the number of words to get the average
    featureVec = np.divide(featureVec,nwords)
    return featureVec


def getAvgFeatureVecs(reviews, model, num_features):
    # Given a set of reviews (each one a list of words), calculate
    # the average feature vector for each one and return a 2D numpy array
    #
    # Initialize a counter
    counter = 0.
    #
    # Preallocate a 2D numpy array, for speed
    reviewFeatureVecs = np.zeros((len(reviews),num_features),dtype="float32")
    #
    # Loop through the reviews
    for review in reviews:
       #
       # Print a status message every 1000th review
       if counter%1000. == 0.:
           print "Review %d of %d" % (counter, len(reviews))
       #
       # Call the function (defined above) that makes average feature vectors
       reviewFeatureVecs[counter] = makeFeatureVec(review, model, \
           num_features)
       #
       # Increment the counter
       counter = counter + 1.
    return reviewFeatureVecs


def getCleanReviews(reviews):
    clean_reviews = []
    for sequence in reviews["sequence"]:
        clean_reviews.append(sequence.lower().split())
    return clean_reviews


def average_vectors(model_name, base, num_features):
    # Read data from files
    train = pd.read_csv(base + "genesTrainDataShuffle.tsv", header=0, delimiter=";", quoting=3)
    test = pd.read_csv(base + "genesTestDataShuffle.tsv", header=0, delimiter=";", quoting=3)

    # Verify the number of reviews that were read
    print "Read %d labeled train reviews and %d labeled test reviews\n" \
          % (train["sequence"].size, test["sequence"].size)



    model = Word2Vec.load(model_name)

    # ****** Create average vectors for the training and test sets
    #
    print "Creating average feature vecs for training reviews"

    trainDataVecs = getAvgFeatureVecs(getCleanReviews(train), model, num_features)

    print "Creating average feature vecs for test reviews"

    testDataVecs = getAvgFeatureVecs(getCleanReviews(test), model, num_features)

    # ****** Fit a random forest to the training set, then make predictions
    #
    # Fit a random forest to the training data, using 100 trees
    forest = RandomForestClassifier(n_estimators=100)

    print "Fitting a random forest to labeled training data..."
    forest = forest.fit(trainDataVecs, train["isgene"])

    # Test & extract results
    result = forest.predict(testDataVecs)

    # Write the test results
    output = pd.DataFrame(data={"id": test["id"], "isgene": result})
    output.to_csv("data/genes/Genes_AverageVectors.csv", index=False, quoting=3)
    print "Wrote Genes_AverageVectors.csv"


# average_vectors("data/genes/hs+nsFullORFskipgram10features_20context_0downsampling", "data/genes/full/")