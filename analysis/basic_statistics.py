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

word_list = list(corpus.words())
vocabulary = set(word_list)

print("len words:" + str(len(word_list)))
print("len vocab:" + str(len(vocabulary)))
print("Text richness: " + str(lexical_diversity(word_list)))
print()

word_list_pop = list(corpus.words(categories="POP"))
vocabulary_pop = set(word_list_pop)

print("len words POP:" + str(len(word_list_pop)))
print("len vocab POP:" + str(len(vocabulary_pop)))
print("Text richness POP: " + str(lexical_diversity(word_list_pop)))
print()

word_list_rock = list(corpus.words(categories="ROCK"))
vocabulary_rock = set(word_list_rock)

print("len words ROCK:" + str(len(word_list_rock)))
print("len vocab ROCK:" + str(len(vocabulary_rock)))
print("Text richness ROCK: " + str(lexical_diversity(word_list_rock)))

print()

