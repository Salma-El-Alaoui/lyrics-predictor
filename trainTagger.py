__author__ = 'qrr'

import nltk
from nltk.corpus import brown
from nltk import NgramTagger
from pickle import dump

#use brown corpus to train our Tagger
train_sents = brown.tagged_sents()

#train Ngram Tagger
def trainTagger(corpus, n):
    tagger = nltk.DefaultTagger('NN')           # NN is the default argument
    for n in range(1, n + 1):                   # start at unigrams (1) up to and including trigrams (n)
        tagger = NgramTagger(n, corpus, backoff = tagger)
    return tagger

#train trigram tagger with backoff
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)

#train trigram tagger without backoff
t3nb = nltk.TrigramTagger(train_sents)

#store trigram tagger with backoff
output = open('t3b.pkl', 'wb')
dump(t3, output, -1)
output.close()

#store trigram tagger without back off
output2 = open('t3nb.pkl', 'wb')
dump(t3nb, output2, -1)
output2.close()

