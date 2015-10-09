__author__ = 'qrr'

import nltk
from nltk.corpus import gutenberg, brown
from nltk.probability import *
import random
from nltk import ngrams



blakePoems = gutenberg.words('blake-poems.txt')


def ngram_freq_dist(corpus, n):
    return nltk.FreqDist(tuple(corpus[i:i+n]) for i in range(len(corpus)-1))

    dist = ngram_freq_dist(blakePoems, 3)

def ngram_freq_cond(corpus, n):
        size = len(corpus)
        cd = ConditionalFreqDist( (tuple(corpus[i-(n-1):i]),corpus[i])  # (history, next character) at position i in training corpus
                for i in range(n-1, size) )
        return cd

def generate_sentence(corpus, n , length = 15):

    fdist = ngram_freq_dist(corpus, n)
    cfdist = ngram_freq_cond(corpus, n)

    countStart = 0
    listContext = []
    for ngram in fdist :
            if ngram[0] == '.' :
                countStart += 1
                listContext.append(ngram)

    seed = random.randrange(0,countStart)
    context = listContext[seed]
    #remove the point
    context = context[1:n]
    for j in range(n-1):
            print(context[j], end = ' ')
    for i in range(length):
        nextWord = cfdist[context].max()
        print(nextWord, end = ' ')
        if (nextWord == '.')|(nextWord == '!')|(nextWord == '?')| (((nextWord == ';')|(nextWord == ',')) & (i > length - 3)):
            break
        context = context[1:n-1]+(nextWord,)


#generate_sentence(blakePoems, 2)
#print("\n")
#generate_sentence(blakePoems, 3)
#print("\n")
#generate_sentence(blakePoems, 4)
#print("\n")
#generate_sentence(blakePoems, 5)

fdist =ngram_freq_dist(['I', 'can', 'do', 'it', 'do'],2 )
cfdist = ngram_freq_cond(['I', 'can', 'do', 'it'], 2)
#cpdist =  ConditionalProbDist(cfdist, MLEProbDist)
#print(cpdist.__getitem__(('I',)).prob('can'))




















