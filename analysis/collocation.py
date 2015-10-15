from nltk.corpus import CategorizedPlaintextCorpusReader
from nltk import bigrams
from nltk.collocations import *
import nltk

corpus_root = "../corpus/lyric_corpus/files/"
cat_root = "../categories/"

# Hacky way to specify path for cat.txt. A better way would be to rewrite regex '.*\.txt'...
corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')

# word lists
word_list = list(corpus.words())
word_list_pop = list(corpus.words(categories="POP"))
word_list_rock = list(corpus.words(categories="ROCK"))

# bigram lists
bigram_list = list(bigrams(word_list))
bigram_list_pop = list(bigrams(word_list_pop))
bigram_list_rock = list(bigrams(word_list_rock))

# measures
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# finders
bi_finder = BigramCollocationFinder.from_words(word_list)
bi_finder_pop = BigramCollocationFinder.from_words(word_list_pop)
bi_finder_rock = BigramCollocationFinder.from_words(word_list_rock)

tri_finder = TrigramCollocationFinder.from_words(word_list)
tri_finder_pop = TrigramCollocationFinder.from_words(word_list_pop)
tri_finder_rock = TrigramCollocationFinder.from_words(word_list_rock)

#finder = TrigramCollocationFinder.from_words(word_list)

# Filter
#creature_filter = lambda *w: 'love' not in w
bi_finder.apply_freq_filter(3)
bi_finder_pop.apply_freq_filter(3)
bi_finder_rock.apply_freq_filter(3)

tri_finder.apply_freq_filter(3)
tri_finder_pop.apply_freq_filter(3)
tri_finder_rock.apply_freq_filter(3)
#bi_finder.apply_ngram_filter(creature_filter)


# Results
result_bi = bi_finder.nbest(bigram_measures.pmi, 40)
result_bi_pop = bi_finder_pop.nbest(bigram_measures.pmi, 40)
result_bi_rock = bi_finder_rock.nbest(bigram_measures.pmi, 40)

result_tri = tri_finder.nbest(trigram_measures.pmi, 40)
result_tri_pop = tri_finder_pop.nbest(trigram_measures.pmi, 40)
result_tri_rock = tri_finder_rock.nbest(trigram_measures.pmi, 40)


print("All Lyrics:")
for i,colloc in enumerate(result_bi):
    print(str(i) + ": " + str(colloc))

print("\nPOP:")
for i,colloc in enumerate(result_bi_pop):
    print(str(i) + ": " + str(colloc))

print("\nROCK:")
for i,colloc in enumerate(result_bi_rock):
    print(str(i) + ": " + str(colloc))

print("\nAll Lyrics:")
for i,colloc in enumerate(result_tri):
    print(str(i) + ": " + str(colloc))

print("\nPOP:")
for i,colloc in enumerate(result_tri_pop):
    print(str(i) + ": " + str(colloc))

print("\nROCK:")
for i,colloc in enumerate(result_tri_rock):
    print(str(i) + ": " + str(colloc))


