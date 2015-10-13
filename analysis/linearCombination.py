__author__ = 'Salma'

#from nGram import NgramTagModel,nGramModel
import corpus.lyric_corpus.corpus_access as corpus
from nGram.NgramTagModel import NgramTagModel

trainCorpus, testCorpus, devCorpus = corpus.loadCorpus()

# print (testCorpus)

tm = NgramTagModel(3,2,trainCorpus)
testTag = tm.tagTestCorpus(testCorpus)
context = tm.getRandomContext(testTag)
print("Context", context)
print(tm.nextWord(context))

# print(sents)




