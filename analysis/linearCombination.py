__author__ = 'Salma'

from nGram import NgramTagModel,nGramModel
import corpus.lyric_corpus.corpus_access as corpus

train, test = corpus.loadCorpus()

print(list(test))




