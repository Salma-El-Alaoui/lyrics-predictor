from nltk.corpus import PlaintextCorpusReader
import os

corpus_root = "./lyrics_clean/"
if not os.name == 'posix':
    corpus_root = ".\\lyrics_clean\\"

# load the corpus
corpus = PlaintextCorpusReader(corpus_root, '.*\.txt')

# print files in corpus
for file in corpus.fileids():
    print(file)

# access corpus
raw = corpus.raw()
words = corpus.words()
sents = corpus.sents()

#for sentence in sents:
#   print(sentence)


# access specific file
words_dancing_queeen = corpus.words("ABBA_Dancing Queen.txt")
sents_dancing_queeen = corpus.sents("ABBA_Dancing Queen.txt")

#for sentence in sents_dancing_queeen:
#   print(sentence)

