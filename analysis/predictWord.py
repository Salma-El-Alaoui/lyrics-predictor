__author__ = 'qrr'

import corpus.lyric_corpus.corpus_access as corpus
from nGram.NgramTagModel import NgramTagModel
import random

def getWordContext(tagSent, n):
    context = []
    wordlist = []
    for word in tagSent:
        wordlist.append(word)
    size = len(wordlist)
    seed = random.randrange(n-1, size)
    for i in range(seed - (n-1), seed):
        context.append(wordlist[i])
    return context, wordlist[seed][0]


corpus, trainCorpus, testCorpus, testSents = corpus.loadCorpus()
# corpus, trainCorpus, testCorpus, testSents = corpus.loadCorpus("POP")
# corpus, trainCorpus, testCorpus, testSents = corpus.loadCorpus("ROCK")

# print (testCorpus)

nTag = 2
nWord = 2
n = max(nTag, nWord)
tm = NgramTagModel(nTag,nWord,trainCorpus)
# testTag = tm.tagTestCorpus(testCorpus)
totalTest = 0
correctTest = 0

for sent in testSents:
    tagSent = tm.tagTestCorpus(sent)
    if(len(list(sent)) >= n):
        print (sent)
        context, correctWord = getWordContext(tagSent, n)
        print (context, correctWord)
        predictWord = tm.nextWord(context)
        totalTest += 1
        if(totalTest >= 100):
            break
        if(predictWord == correctWord):
            correctTest += 1
print ("TotalTest", totalTest)
print ("CorrectTest", correctTest)
# print("Context", context)
# print(tm.nextWord(context))
