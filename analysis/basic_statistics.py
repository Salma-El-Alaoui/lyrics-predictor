import nltk
from nltk.corpus import CategorizedPlaintextCorpusReader
from nltk.corpus import brown

corpus_root = "../corpus/lyric_corpus/files/"
cat_root = "../categories/"

# basic measures taken from nltk book
def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total


# Hacky way to specify path for cat.txt. A better way would be to rewrite regex '.*\.txt'...
corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')

# NLTK brow selection
word_list_brown = brown.words()
sents_list_brown = brown.sents()
vocabulary_brown = set(word_list_brown)
brown_len_words = len(word_list_brown)
brown_len_sents = len(sents_list_brown)
brown_len_vocab = len(vocabulary_brown)
brown_richness = lexical_diversity(word_list_brown)

# Lyric corpus
cats = corpus.categories()

num_files = len(corpus.fileids())
word_list = list(corpus.words())
sents_list = list(corpus.sents())
vocabulary = set(word_list)
total_len_words = len(word_list)
total_len_sents = len(sents_list)
total_len_vocab = len(vocabulary)
total_richness = lexical_diversity(word_list)

# POP
word_list_pop = list(corpus.words(categories="POP"))
sents_list_pop = list(corpus.sents(categories="POP"))
vocabulary_pop = set(word_list_pop)
pop_len_words = len(word_list_pop)
pop_len_sents = len(sents_list_pop)
pop_len_vocab = len(vocabulary_pop)
pop_richness = lexical_diversity(word_list_pop)

# ROCK
word_list_rock = list(corpus.words(categories="ROCK"))
sents_list_rock = list(corpus.sents(categories="ROCK"))
vocabulary_rock = set(word_list_rock)
rock_len_words = len(word_list_rock)
rock_len_sents = len(sents_list_rock)
rock_len_vocab = len(vocabulary_rock)
rock_richness = lexical_diversity(word_list_rock)

# Britney Spears
word_list_spears = list(corpus.words(categories="BritneySpears"))
spears_len_words = len(word_list_spears)
spears_richness = lexical_diversity(word_list_spears)

# The Rolling Stones
word_list_stones = list(corpus.words(categories="TheRollingStones"))
stones_len_words = len(word_list_stones)
stones_richness = lexical_diversity(word_list_stones)


print("Brown words: " + str(brown_len_words))
print("Brown sents: " + str(brown_len_sents))
print("Brown vocab: " + str(brown_len_vocab))
print("Brown richness: " + str(brown_richness))
print()

print("Total files " + str(num_files))
print("Lyric words: " + str(total_len_words) + " check: " + str(pop_len_words+rock_len_words))
print("Lyric sents: " + str(total_len_sents) + " check: " + str(pop_len_sents+rock_len_sents))
print("Lyric vocab: " + str(total_len_vocab))
print("Lyric richness: " + str(total_richness))
print()

print("Pop words: " + str(pop_len_words))
print("Pop sents: " + str(pop_len_sents))
print("Pop vocab: " + str(pop_len_vocab))
print("Pop richness: " + str(pop_richness))
print()

print("Rock words: " + str(rock_len_words))
print("Rock sents: " + str(rock_len_sents))
print("Rock vocab: " + str(rock_len_vocab))
print("Rock richness: " + str(rock_richness))
print()

print("Spears words: " + str(spears_len_words))
print("Spears richness: " + str(spears_richness))
print("Stones words: " + str(stones_len_words))
print("Stones richness: " + str(stones_richness))

# chart the stuff

total_fd = nltk.FreqDist(word_list).most_common(50)
for e in total_fd:
    print(e)