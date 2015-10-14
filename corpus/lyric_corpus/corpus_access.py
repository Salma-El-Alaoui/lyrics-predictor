from nltk.corpus import PlaintextCorpusReader
import os
import random
import math
def loadCorpus() :

    corpus_root = "../corpus/lyric_corpus/files/"

    if not os.name == 'posix':
        corpus_root = "..\\corpus\\lyric_corpus\\files\\"
    # load the corpus

    corpus = PlaintextCorpusReader(corpus_root, '.*\.txt')
    # print files in corpus
    # for file in corpus.fileids():
    # print(file)
    # access corpus

    raw = corpus.raw()
    words = corpus.words()
    sents = corpus.sents()

    shuffledSents = shuffleSent(sents)


    numberSents = len(shuffledSents)
    trainSize = math.floor(numberSents*0.8)
    testSize = math.floor(numberSents*0.1)
    devSize = len(shuffledSents)-trainSize - testSize

    trainCorpus = []
    testCorpus = []
    devCorpus = []

    for i in range(numberSents):
        if(i < trainSize):
            for word in shuffledSents[i]:
                trainCorpus.append(word)
        elif(i < (trainSize + testSize)):
            for word in shuffledSents[i]:
                testCorpus.append(word)
        else:
            for word in shuffledSents[i]:
                devCorpus.append(word)



    # testCorpus = []
    # trainCorpus = list(words)
    # for i in range(testSize):
    #     seed = random.randrange(0,numberSents - i)
    #     testCorpus.append(trainCorpus.pop(seed))

    return trainCorpus, testCorpus, devCorpus

def shuffleSent(sents):
    sentsList = list(sents)
    random.shuffle(sentsList)
    return sentsList

# for sentence in sents:
#   print(sentence)


# access specific file
# words_dancing_queeen = corpus.words("ABBA_Dancing Queen.txt")
# sents_dancing_queeen = corpus.sents("ABBA_Dancing Queen.txt")

# for sentence in sents_dancing_queeen:
#   print(sentence)
