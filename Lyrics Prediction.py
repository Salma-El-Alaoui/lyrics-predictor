__author__ = 'qrr'

import nltk
from nltk.corpus import brown

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max()

text = nltk.corpus.brown.words('cb13')
# text = brown.words()
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

print cfd['People']

generate_model(cfd, 'People')


# from nltk.corpus import brown
# print brown.words()
