__author__ = 'qrr'

import nltk
from nltk.corpus import gutenberg
from nltk import NgramTagger
from nltk.probability import *
from pickle import load

class NgramTagModel:

    def __init__(self, n, trainingCorpus):

        self._n = n

        #if change n, then the file name should be modified
        input = open('t3b.pkl', 'rb')
        tagger = load(input)
        self._tagger = tagger
        input.close()

        #tag our own training corpus using trained Ngram Tagger
        taggedTrainingCorpus = tagger.tag(trainingCorpus)

        # find all tags, tagList (now replaced by self._cFdist)
        # tagList = []
        # for taggedWord in taggedTrainingCorpus:
        #     if taggedWord[1] not in tagList:
        #         tagList.append(taggedWord[1])
        # self._tagList = tagList

        size = len(taggedTrainingCorpus)

        #count conditional prob for tags, p(ti|ti-1,ti-2), only for Trigram now!!!
        cfdistTag = ConditionalFreqDist(((x[1], y[1]), z[1])
                                       for x, y, z in nltk.trigrams(taggedTrainingCorpus))

        # need to modify below code to fit into Ngram
        # cfdistTag = ConditionalFreqDist((tuple(taggedTrainingCorpus[i-(n-1):i][1]), taggedTrainingCorpus[i][1])
        #         for i in range(n-1, size))

        self._cFdistTag = cfdistTag
        cpdistTag =  ConditionalProbDist(cfdistTag, MLEProbDist)
        self._probDistTag = cpdistTag

        #count conditional prob for p(wi|ti)
        cfdist = ConditionalFreqDist((taggedTrainingCorpus[i][1], taggedTrainingCorpus[i][0])
                for i in range(size))
        self._cFdist = cfdist
        cpdist =  ConditionalProbDist(cfdist, MLEProbDist)
        self._probDist = cpdist


    #calculate p(wi|ti)*p(ti|ti-1,ti-2)
    def probCondMulti(self, word, tag, context):
        context = tuple(context)
        wordProb = self._probDist.__getitem__(tag).prob(word)
        tagProb = self._probDistTag.__getitem__(context).prob(tag)
        return (wordProb * tagProb)


    #give wi,ti-2, ti-2, find the max {p(wi|ti)*p(ti|ti-1,ti-2)}
    def nextWordTag(self, word, context):
        maxValue = -1
        for tag in self._cFdist:
            if(self._probDist.__getitem__(tag).prob(word) != 0):
                tmpValue = self.probCondMulti(word, tag, context)
                if(tmpValue > maxValue):
                    maxValue = tmpValue
        return maxValue


blakePoems = gutenberg.words('blake-poems.txt')
tm = NgramTagModel(3,blakePoems)
# print (list(tm._probDistTag))
print (tm.probCondMulti('bed', 'NN', ('IN','AT')))
print (tm.nextWordTag('bed', ('IN','AT')))
