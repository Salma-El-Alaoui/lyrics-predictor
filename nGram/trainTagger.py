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
t4 = nltk.NgramTagger(4, train_sents, backoff=t3)

#train trigram tagger without backoff
# t3nb = nltk.TrigramTagger(train_sents)

#store gram tagger with backoff
output0 = open('t0.pkl', 'wb')
dump(t0, output0, -1)
output0.close()

output1 = open('t1.pkl', 'wb')
dump(t1, output1, -1)
output1.close()

output2 = open('t2.pkl', 'wb')
dump(t2, output2, -1)
output2.close()

output3 = open('t3.pkl', 'wb')
dump(t3, output3, -1)
output3.close()

output4 = open('t4.pkl', 'wb')
dump(t4, output4, -1)
output4.close()

#store trigram tagger without back off
# output2 = open('t3nb.pkl', 'wb')
# dump(t3nb, output2, -1)
# output2.close()

