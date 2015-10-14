from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import CategorizedPlaintextCorpusReader
import os
import random
import math
def loadCorpus(category = None) :

    corpus_root = "../corpus/lyric_corpus/files/"
    cat_root = "../categories/"

    if not os.name == 'posix':
        corpus_root = "..\\corpus\\lyric_corpus\\files\\"
    # load the corpus

    # corpus = PlaintextCorpusReader(corpus_root, '.*\.txt')
    corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')
    # print files in corpus
    # for file in corpus.fileids():
    # print(file)
    # access corpus

    raw = corpus.raw()
    words = corpus.words()
    print (category)
    if(category == None):
        sents = corpus.sents()
    else:
        sents = corpus.sents(categories = category)
    # sents_pop = corpus.sents(categories="POP")
    # sents_rock = corpus.sents(categories="ROCK")

    shuffledSents = shuffleSent(sents)


    numberSents = len(shuffledSents)
    trainSize = math.floor(numberSents*0.8)
    testSize = math.floor(numberSents*0.1)
    devSize = len(shuffledSents)-trainSize - testSize

    trainCorpus = []
    testCorpus = []
    devCorpus = []
    wholeCorpus = []

    for i in range(numberSents):
        if(i < trainSize):
            for word in shuffledSents[i]:
                trainCorpus.append(word)
                wholeCorpus.append(word)
        elif(i < (trainSize + testSize)):
            for word in shuffledSents[i]:
                testCorpus.append(word)
                wholeCorpus.append(word)
        else:
            for word in shuffledSents[i]:
                devCorpus.append(word)
                wholeCorpus.append(word)



    # testCorpus = []
    # trainCorpus = list(words)
    # for i in range(testSize):
    #     seed = random.randrange(0,numberSents - i)
    #     testCorpus.append(trainCorpus.pop(seed))

    return wholeCorpus, trainCorpus, testCorpus, devCorpus

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
