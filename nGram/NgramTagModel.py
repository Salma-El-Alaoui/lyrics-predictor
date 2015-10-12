__author__ = 'qrr'

from pickle import load
import random

import nltk
from nltk.corpus import gutenberg
from nltk.probability import *

from nGram.nGramModel import NgramModel


class NgramTagModel:

    def __init__(self, nTag, nWord, trainingCorpus):

        self._nTag = nTag
        self._nWord = nWord
        #if change n, then the file name should be modified
        input = open('../taggers/t3b.pkl', 'rb')
        tagger = load(input)
        self._tagger = tagger
        print(tagger)
        input.close()

        self._ngram = NgramModel(nWord, trainingCorpus)
        #tag our own training corpus using trained Ngram Tagger
        taggedTrainingCorpus = self._tagger.tag(trainingCorpus)

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

    def linearCombination(self, contextWords, contextTags):

        contextWords = contextWords[len(contextWords) - (self._nWord-1) : len(contextWords)]
        contextTags = contextTags[len(contextTags) - (self._nTag-1) : len(contextTags)]
        alpha = 0.5
        print("CONTEXT WORDS", contextWords)
        print("CONTEXT TAGS", contextTags)
        nextWords = self._ngram.wordsInContext(contextWords)
        print("NEXT WORDS", nextWords)
        maxValue = -1
        maxWord = ""
        for word in nextWords :
            prob = alpha * self._ngram.prob(word, contextWords) + (1-alpha)* self.nextWordTag(word, contextTags)
            if(prob > maxValue):
                    maxValue = prob
                    maxWord = word
        return maxWord

    def tagTestCorpus(self, testCorpus):
        return self._tagger.tag(testCorpus)

    def getRandomContext(self, testCorpus):
        numWords = max(self._nWord, self._nTag)
        size = len(testCorpus)
        seed = random.randrange(0,size-numWords-1)
        context = testCorpus[seed: seed+numWords-1]
        return(context)

    def nextWord(self, context):
        size = len(context)
        listWords = [context[i][0]for i in range(size)]
        listTags = [context[i][1]for i in range(size)]
        return self.linearCombination(listWords, listTags)

blakePoems = gutenberg.words('blake-poems.txt')

size = int(len(blakePoems) * 0.8)
train = blakePoems[:size]
test = blakePoems[size:]

tm = NgramTagModel(3,2,train)
testTag = tm.tagTestCorpus(test)
context = tm.getRandomContext(testTag)
print("Context", context)
print(tm.nextWord(context))

# print (list(tm._probDistTag))
#print (tm.probCondMulti('bed', 'NN', ('IN','AT')))
#print (tm.nextWordTag('bed', ('IN','AT')))
