__author__ = 'qrr'

import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
# print brown_tagged_sents
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents) * 0.8)

train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unseen_sents = brown_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)
# print t2.tag(brown_sents[2007])
# print t2.tag(unseen_sents)

for word in unseen_sents:
    print t3.tag(word)

print t2.evaluate(test_sents)
print t3.evaluate(test_sents)