__author__ = 'Salma'

import nltk
from nltk.corpus import gutenberg
from nltk.probability import *
import random
from math import log

class NgramModel :

    """
        Creates an N-Gram language model.
        :param estimator: distribution to smooth the probabilities derived from the training corpus
        if no estimator is specified, the N-gram model uses the MLE estimator
        possible estimators:
         * MLEProbDist
         * LaplaceProbDist : LaPlace smoothing. Optional parameter: number of bins
         * LidstoneProbDist : Lidstone smoothing. Parameters: gamma, bins (optional)
         *

        :type:
        : estimator_args: additional parameter for the chosen probability distribution (like the number of bins


    """
    def __init__(self, n, trainingCorpus, estimator, *estimator_args, **estimator_kwargs):

        self._n = n
        size = len(trainingCorpus)
        fdist = FreqDist(tuple(trainingCorpus[i:i+n]) for i in range(len(trainingCorpus)-1))
        self._fDist = fdist
        cfdist = ConditionalFreqDist((tuple(trainingCorpus[i-(n-1):i]), trainingCorpus[i])
                for i in range(n-1, size))
        self._cFdist = cfdist

        if estimator is None :
        #if no estimator is defined, the default is the MLE estimator
            cpdist =  ConditionalProbDist(cfdist, MLEProbDist)
        else :
            cpdist = ConditionalProbDist(cfdist, estimator, *estimator_args, **estimator_kwargs)
        self._probDist = cpdist


    def prob(self, word, context):
        context = tuple(context)
        if self._probDist.__getitem__(context) is None :
            return 0
        else :
            return self._probDist.__getitem__(context).prob(word)

    def nextWord(self, context):
        context = tuple(context)
        return self._probDist.__getitem__(context).max()

    def generateRandomContext(self):
        countStart = 0
        listContext = []
        for ngram in self._fDist :
            if ngram[0] == '.' :
                countStart += 1
                listContext.append(ngram)
        seed = random.randrange(0,countStart)
        context = listContext[seed]
        #remove the point
        context = context[1:self._n]
        return list(context)

    def generateRandomSentence(self, length = 15):
        sentence = self.generateRandomContext()
        context = tuple(sentence)
        for i in range(length):
            nextWord = self.nextWord(context)
            sentence.append(nextWord)
            if (nextWord == '.')|(nextWord == '!')|(nextWord == '?')| (((nextWord == ';')|(nextWord == ',')) & (i > length - 3)):
                break
            context = context[1:self._n-1]+(nextWord,)
        return sentence

    """
        log probability of this word in this context.

        :param word: the word to get the probability of
        :type word: str
        :param context: the context the word is in
        :type context: list(str)
    """
    def logProb(self, word, context):

        if self.prob(word, context) is None :
            return 0
        else :
            return log(self.prob(word, context), 2)


    """
    Calculates the perplexity of the n-gram model for a
    given evaluation text.
    This is the average log probability of each word in the text.

    :param corpus: test corpus
    :type text: list(str)
    """
    def perplexity(self, corpus):
        e = 0.0
        for i in range(self._n - 1, len(corpus)):
            context = tuple(corpus[i-(self._n-1):i])
            token = corpus[i]
            e += self.logProb(token, context)
        return e / float(len(corpus))





blakePoems = gutenberg.words('blake-poems.txt')
size = int(len(blakePoems) * 0.8)
train = blakePoems[:size]
test = blakePoems[size:]

lm = NgramModel( 3,train, LaplaceProbDist)
#lm.perplexity(test)
#print(lm.prob('love', ['I','can']))
#print(lm.nextWord(['I','can']))
print(lm.generateRandomContext())
print(lm.generateRandomSentence())
#est = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)

