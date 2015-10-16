__author__ = 'Salma'

import corpus.lyric_corpus.corpus_access as corpus
from nGram.NgramTagModel import NgramTagModel
from nGram.nGramModel import NgramModel
from nltk.probability import *
import random
import nltk.corpus

#song corpus
corpus, trainCorpus, testCorpus, testSents = corpus.loadCorpus()

#brow corpus for comaprison
brown = nltk.corpus.brown.words()

size = int(len(brown) * 0.8)
trainBrown = brown[:size]
testBrown = brown[size:]

#Perplexity for different N-grams with back-off
for i in range(1,5):
    if i==1:
        lm1 = NgramModel( i,trainCorpus, LaplaceProbDist, False, False)
        lm2 = NgramModel(i, trainCorpus, LaplaceProbDist, False, False)
    else :
        lm1 = NgramModel( i,trainCorpus, MLEProbDist, False, True)
        lm2 = NgramModel(i, trainCorpus, MLEProbDist, False, True)
    print("N-gram :", i)
    print("Brown perplexity: ", lm1.perplexity(testBrown))
    print("Song corpus: ", lm2.perplexity(testCorpus))

