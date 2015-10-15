__author__ = 'qrr'

import corpus.lyric_corpus.corpus_access as corpus
from nGram.nGramModel import NgramModel
from nltk.probability import *

corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus()
# corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus("POP")
# corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus("ROCK")

lm = NgramModel(2, corpus, WittenBellProbDist, True)
# lm = NgramModel(2, corpus)
vocabularyNum = len(set(corpus))
testSent = ['and', 'i', 'do', 'not', 'wanna', 'miss', 'a', 'thing']
size = len(testSent)

# print (lm._fDist)
# print (lm._fDist.__getitem__(('and', 'i')))
# print (lm._probDist.conditions())

# print (lm._probDist.__getitem__(('and',)).samples())
# print (LaplaceProbDist(lm._fDist).freqdist())
# smoothFre = LaplaceProbDist(lm._fDist).freqdist()
for i in range(size):
    for j in range(size):
        print (testSent[i], testSent[j], lm._fDist.__getitem__((testSent[i], testSent[j])),
               lm._probDist.__getitem__((testSent[i],)).prob(testSent[j]))


