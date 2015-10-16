__author__ = 'qrr'

import corpus.lyric_corpus.corpus_access as corpus
from nGram.NgramTagModel import NgramTagModel
import random
import math

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


# corpus, trainCorpus, testCorpus, testSents = corpus.loadCorpus()
# corpus, trainCorpus, testCorpus, testSents = corpus.loadCorpus("POP")
corpus, trainCorpus, testCorpus, testSents = corpus.loadCorpus("ROCK")

# print (testCorpus)

nTag = 2
nWord = 4
n = max(nTag, nWord)
# tm = NgramTagModel(nTag,nWord,trainCorpus)
# testTag = tm.tagTestCorpus(testCorpus)
print ("nTag", nTag, "nWord", nWord)
size = len(testSents)
validationSize = math.floor(size*0.5)
testSize = size - validationSize
validationSents = []
newTestSents = []
for i in range(validationSize):
    validationSents.append(testSents[i])
for i in range(validationSize, size):
    newTestSents.append(testSents[i])
alpha = 0.1
while alpha <= 1:
    tm = NgramTagModel(nTag,nWord,trainCorpus, alpha)
    i = 0
    totalValidation = 0
    correctValidation = 0
    random.shuffle(validationSents)
    random.shuffle(newTestSents)
    for sent in validationSents:
        if(len(list(sent)) >= n):
            tagSent = tm.tagTestCorpus(sent)
            # print (testSents[i])
            context, correctWord = getWordContext(tagSent, n)
            # print (context, correctWord)
            predictWord = tm.nextWord(context)
            # print (predictWord)
            totalValidation += 1
            if(predictWord == correctWord):
                correctValidation += 1
            if(totalValidation >= 200):
                break
    totalTest = 0
    correctTest = 0
    for sent in testSents:
        if(len(list(sent)) >= n):
            tagSent = tm.tagTestCorpus(sent)
            # print (testSents[i])
            context, correctWord = getWordContext(tagSent, n)
            # print (context, correctWord)
            predictWord = tm.nextWord(context)
            # print (predictWord)
            totalTest += 1
            if(predictWord == correctWord):
                correctTest += 1
            if(totalTest >= 200):
                break
    print ("alpha:", alpha)
    print ("TotalValidation", totalValidation, "CorrectValidation", correctValidation, "Accuracy", correctValidation/totalValidation)
    print ("TotalTest", totalTest, "CorrectTest", correctTest, "Accuracy", correctTest/totalTest)
    alpha += 0.1

# print("Context", context)
# print(tm.nextWord(context))
