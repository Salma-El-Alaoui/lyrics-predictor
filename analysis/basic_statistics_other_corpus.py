import nltk.corpus

brown = nltk.corpus.brown
guten = nltk.corpus.gutenberg

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total


word_list_brown = list(brown.words())
vocabulary_brown = set(word_list_brown)

print("len words for brown:" + str(len(word_list_brown)))
print("len vocab for brown:" + str(len(vocabulary_brown)))
print("Text richness for brown: " + str(lexical_diversity(word_list_brown)))

print()

word_list_guten = list(guten.words())
vocabulary_guten = set(word_list_guten)

print("len words for guten:" + str(len(word_list_guten)))
print("len vocab for guten:" + str(len(vocabulary_guten)))
print("Text richness for guten: " + str(lexical_diversity(word_list_guten)))

print()