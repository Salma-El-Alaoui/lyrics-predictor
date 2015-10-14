__author__ = 'qrr'

#generate random sentence using simple N-gram
#do experiments and compare using different N and different corpus

import corpus.lyric_corpus.corpus_access as corpus
from nGram.nGramModel import NgramModel

# corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus()
# corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus("POP")
corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus("ROCK")

lm = NgramModel(4, corpus)
vocabularyNum = len(set(corpus))
print ("vocabulary number:", vocabularyNum)
print ("4-gram")
for i in range(15):
    print (lm.generateRandomSentence())



