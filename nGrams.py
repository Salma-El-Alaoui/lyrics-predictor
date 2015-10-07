__author__ = 'qrr'

import nltk
from nltk.corpus import gutenberg
from nltk.probability import *

from random import randint


blakePoems = gutenberg.words('blake-poems.txt')

def ngram_freq_dist(corpus, n):
    return nltk.FreqDist(tuple(corpus[i:i+n]) for i in range(len(corpus)-1))

dist = ngram_freq_dist(blakePoems, 3)

def ngram_freq_cond(corpus, n):
        size = len(corpus)
        cd = ConditionalFreqDist( (tuple(corpus[i-(n-1):i]),corpus[i])  # (history, next character) at position i in training corpus
                for i in range(n-1, size) )
        return cd

def generate_model(cfdist, context, num=15):
    seed = randint(0,9)
    n = len(context)
    for j in range(n):
            print(context[j], end = ' ')
    for i in range(num):
        nextWord = cfdist[context].max()
        print(nextWord, end = ' ')
        context = context[1:n]+(nextWord,)

bigramCfd = ngram_freq_cond(blakePoems, 2)
trigramCfd = ngram_freq_cond(blakePoems, 3)
generate_model(bigramCfd, ('I',))
print("\n")
generate_model(trigramCfd, ('I','am'))
generate_model()

















