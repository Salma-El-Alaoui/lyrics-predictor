__author__ = 'qrr'

import corpus.lyric_corpus.corpus_access as corpus
from nGram.NgramTagModel import NgramTagModel

corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus()
# corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus("POP")
# corpus, trainCorpus, testCorpus, devCorpus = corpus.loadCorpus("ROCK")

# print (testCorpus)

tm = NgramTagModel(3,2,trainCorpus)
testTag = tm.tagTestCorpus(testCorpus)
context = tm.getRandomContext(testTag)
print("Context", context)
print(tm.nextWord(context))
