from nltk.corpus import CategorizedPlaintextCorpusReader

corpus_root = "../corpus/lyric_corpus/files/"
cat_root = "../categories/"

# basic measures taken from nltk book
def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total


# Hacky way to specify path for cat.txt. A better way would be to rewrite regex '.*\.txt'...
corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')

print(corpus.categories())


# word_list_ABBA = list(corpus.words(categories="ABBA"))
# vocabulary_ABBA = set(word_list_ABBA)`
#
# print("len words ABBA:" + str(len(word_list_ABBA)))
# print("len vocab ABBA:" + str(len(vocabulary_ABBA)))
# print("Text richness ABBA: " + str(lexical_diversity(word_list_ABBA)))
# print()
#

SingerWhoAlwaysRepeat = ""
value = 1

for singer in corpus.categories():
    if singer != "ROCK" and singer != "POP":
        print("Artist data is: " + singer)
        word_list = list(corpus.words(categories=singer))
        vocabulary = set(word_list)
        if(value > lexical_diversity(word_list)):
            value = lexical_diversity(word_list)
            SingerWhoAlwaysRepeat = singer
        print("len words:" + str(len(word_list)))
        print("len vocab:" + str(len(vocabulary)))
        print("Text richness: " + str(lexical_diversity(word_list)))
#word_list_%s = "sfsdfsd" % nogthin

print()
print("Singer with always repeat is :" + SingerWhoAlwaysRepeat)