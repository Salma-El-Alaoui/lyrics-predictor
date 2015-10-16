from nltk.corpus import CategorizedPlaintextCorpusReader
from nltk import bigrams
from nltk import trigrams
from nltk.collocations import *
import nltk

corpus_root = "../corpus/lyric_corpus/files/"
cat_root = "../categories/"

# Hacky way to specify path for cat.txt. A better way would be to rewrite regex '.*\.txt'...
corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')

# word lists
word_list_pop = list(corpus.words(categories="POP"))
word_list_rock = list(corpus.words(categories="ROCK"))

# bigram lists
bigram_list_pop = list(bigrams(word_list_pop))
bigram_list_rock = list(bigrams(word_list_rock))

# trigram lists
trigram_list_pop = list(trigrams(word_list_pop))
trigram_list_rock = list(trigrams(word_list_rock))

# measures
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# finders default window size is 2
bi_finder_pop = BigramCollocationFinder.from_words(word_list_pop)
bi_finder_rock = BigramCollocationFinder.from_words(word_list_rock)

# default windwos size is 3
tri_finder_pop = TrigramCollocationFinder.from_words(word_list_pop)
tri_finder_rock = TrigramCollocationFinder.from_words(word_list_rock)


# Filter
f_bi = 10
f_tri = 5
bi_finder_pop.apply_freq_filter(f_bi)
bi_finder_rock.apply_freq_filter(f_bi)

tri_finder_pop.apply_freq_filter(f_tri)
tri_finder_rock.apply_freq_filter(f_tri)


# Results
num_results = 10
result_bi_pop = bi_finder_pop.nbest(bigram_measures.pmi, num_results)
result_bi_rock = bi_finder_rock.nbest(bigram_measures.pmi, num_results)

result_tri_pop = tri_finder_pop.nbest(trigram_measures.pmi, num_results)
result_tri_rock = tri_finder_rock.nbest(trigram_measures.pmi, num_results)


# Scores
scores_bi_pop  = bi_finder_pop.score_ngrams(bigram_measures.pmi)
scores_bi_rock  = bi_finder_rock.score_ngrams(bigram_measures.pmi)

scores_tri_pop  = tri_finder_pop.score_ngrams(trigram_measures.pmi)
scores_tri_rock  = tri_finder_rock.score_ngrams(trigram_measures.pmi)

fd_bi_pop = nltk.FreqDist(bigram_list_pop)
fd_bi_rock = nltk.FreqDist(bigram_list_rock)
fd_tri_pop = nltk.FreqDist(trigram_list_pop)
fd_tri_rock= nltk.FreqDist(trigram_list_rock)

# print results
print("\n Bi_pop:")
for x in range(0,num_results):
    bi = scores_bi_pop[x][0]
    print( str(scores_bi_pop[x]) + " " + str(fd_bi_pop[bi]))

print("\n Bi Rock:")
for x in range(0,num_results):
    bi = scores_bi_rock[x][0]
    print( str(scores_bi_rock[x]) + " " + str(fd_bi_rock[bi]))

print("\n Tri Pop:")
for x in range(0,num_results):
    tri = scores_tri_pop[x][0]
    print( str(scores_tri_pop[x]) + " " + str(fd_tri_pop[tri]))

print("\n Tri Rock:")
for x in range(0,num_results):
    tri = scores_tri_rock[x][0]
    print( str(scores_tri_rock[x]) + " " + str(fd_tri_rock[tri]))

