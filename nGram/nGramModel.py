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
        def __init__(self, n, trainingCorpus, estimator = MLEProbDist, bins = False, backOff = False):
            self._backOff = backOff
            self._n = n
            size = len(trainingCorpus)
            fdist = FreqDist(tuple(trainingCorpus[i:i+n]) for i in range(len(trainingCorpus)))
            cfdist = ConditionalFreqDist((tuple(trainingCorpus[i-(n-1):i]), trainingCorpus[i])
                    for i in range(n-1, size))
            self._fDist = fdist
            self._cFdist = cfdist
            self._T = self._fDist.B()+1
            if (bins) :
                cpdist = ConditionalProbDist(cfdist, estimator, self._T +1 )
            else :
                 cpdist = ConditionalProbDist(cfdist, estimator)
            self._probDist = cpdist
            #print(self._probDist.__getitem__(()).prob('she'))
            test = self._cFdist.conditions()
            #back of n_gram models
            # if our model is not a unigram
            if (backOff):
                if n != 1 :
                    self._alphas = dict()
                    print(self._cFdist.conditions())
                    for context in test:
                            print("context", context)
                            print("next", context[1:])
                            backOff_context = context[1:]
                            backOff_total_pr = 0.0
                            total_observed_pr = 0.0

                            self._backOff = NgramModel(n-1, trainingCorpus, estimator, bins, backOff)
                            #these are the words that could follow our context, ie
                            for word in self.wordsInContext(context):
                                backOff_total_pr += self._backOff.prob(word, backOff_context)
                                total_observed_pr += self.prob(word, context)
                            # beta is the left over probability computed by subtracting from 1 the total probability of observed words
                            beta = 1.0 - total_observed_pr
                            alpha = beta / (1.0-backOff_total_pr)
                            self._alphas[context] = alpha



        def prob(self, word, context=()):
            context = tuple(context)
            print("I'm here" , context)
            freq = self._fDist.__getitem__(context)
            if (freq != 0) | (self._backOff == False) | (self._n==1) :
                return self._probDist.__getitem__(context).prob(word)
            else:
                print("hello", context[1:])
                return self._alphas[context]*self._backOff.prob(word, context[1:])

        def nextWord(self, context=()):
            context = tuple(context)
            return self._probDist.__getitem__(context).max()

        def wordsInContext(self, context=()):
            context = tuple(context)
            nextWords = []
            for word in (self._probDist.__getitem__(context).samples()):
                nextWords.append(word)
            return nextWords

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
            return [context[i] for i in range(len(context))]

        def generateRandomSentence(self, length = 15):
            sentence = self.generateRandomContext()
            context = tuple(sentence)
            for i in range(length):
                nextWord = self.nextWord(context)
                sentence.append(nextWord)
                if ((nextWord == '.') & (i > length - 10)) |((nextWord == '!') & (i > length - 10))|((nextWord == '?')& (i > length - 10))| (i > length - 3):
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

#size = int(len(blakePoems) * 0.8)
#train = blakePoems[:size]
#test = blakePoems[size:]

lm = NgramModel( 2 ,blakePoems)
#lm = NgramModel( 3 ,blakePoems,WittenBellProbDist, True, True)
#print(lm.nextWord('I'))
#print(lm.prob('crazy', ['I','can']))
#print(lm.wordsInContext())
#list = lm.wordsInContext(['I', 'can'])
#lm.perplexity(test)
#print(lm.nextWord(['I','can']))
#print(lm.generateRandomContext())
print(lm.generateRandomSentence())
#est = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)

