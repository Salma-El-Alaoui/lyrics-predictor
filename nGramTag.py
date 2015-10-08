__author__ = 'qrr'

import nltk
from nltk.corpus import brown
from nltk import NgramTagger
from nltk.probability import *

brown_tagged_sents = brown.tagged_sents(categories='news')
# print brown_tagged_sents
brown_sents = brown.sents(categories='news')

# print (list(brown_sents))

size = int(len(brown_tagged_sents) * 0.8)

train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unseen_sents = brown_sents[size:]

def ngramtag_freq_cond(corpus, n = 3):
        cfd = nltk.ConditionalFreqDist(((x[1], y[1], z[0]), z[1])
                                       for sent in corpus
                                       for x, y, z in nltk.trigrams(sent))
        return cfd

def trainTagger(corpus, n):
    tagger = nltk.DefaultTagger('NN')           # NN is the default argument
    for n in range(1, n + 1):                   # start at unigrams (1) up to and including trigrams (n)
        tagger = NgramTagger(n, corpus, backoff = tagger)
    return tagger

# t0 = nltk.DefaultTagger('NN')
# t1 = nltk.UnigramTagger(train_sents, backoff=t0)
# t2 = nltk.BigramTagger(train_sents, backoff=t1)
# t3 = nltk.TrigramTagger(train_sents, backoff=t2)

# print t2.tag(brown_sents[2007])
# print t2.tag(unseen_sents)

# for word in unseen_sents:
    # print (tagger.tag(word))

# print (t2.evaluate(test_sents))
# print (t3.evaluate(test_sents))

tagger = trainTagger(train_sents, 3)
print (tagger.evaluate(test_sents))
print (tagger.tag(brown_sents[4203]))

cfd = ngramtag_freq_cond(train_sents)
print (brown_tagged_sents[4023])
print (brown_tagged_sents[4023][0])

for sent in test_sents:
    for x,y,z in nltk.trigrams(sent):
        if len(cfd[x[1], y[1], z[0]]) > 2:
            mytag = cfd[x[1], y[1], z[0]].max()
            print (x[1], y[1], z[0], mytag, cfd[x[1], y[1], z[0]][mytag])
            for c in cfd[x[1], y[1], z[0]]:
                print (c, cfd[x[1], y[1], z[0]][c])