from nltk.corpus import PlaintextCorpusReader
import os
import random
import math
def loadCorpus() :

    corpus_root = "../corpus/lyric_corpus/lyrics_clean/"

    if not os.name == 'posix':
        corpus_root = "..\\corpus\\lyric_corpus\\lyrics_clean\\"
    # load the corpus

    corpus = PlaintextCorpusReader(corpus_root, '.*\.txt')
    # print files in corpus
    # for file in corpus.fileids():
    # print(file)
    # access corpus

    raw = corpus.raw()
    words = corpus.words()
    sents = corpus.sents()

    numberSents = len(sents)
    trainSize = math.floor(numberSents*0.8)
    testSize = len(sents)-trainSize

    testCorpus = []
    trainCorpus = list(words)
    for i in range(testSize):
        seed = random.randrange(0,numberSents - i)
        testCorpus.append(trainCorpus.pop(seed))

    return words, sents

# for sentence in sents:
#   print(sentence)


# access specific file
# words_dancing_queeen = corpus.words("ABBA_Dancing Queen.txt")
# sents_dancing_queeen = corpus.sents("ABBA_Dancing Queen.txt")

# for sentence in sents_dancing_queeen:
#   print(sentence)
