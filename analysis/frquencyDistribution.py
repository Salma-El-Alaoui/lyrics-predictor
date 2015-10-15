import nltk
from nltk.corpus import CategorizedPlaintextCorpusReader

corpus_root = "../corpus/lyric_corpus/files/"
cat_root = "../categories/"

corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')
words = corpus.words()
#frequency distribution

popWords = corpus.words(categories="POP")
rockWords = corpus.words(categories="ROCK")

print("-----All words-----")
fd = nltk.FreqDist(words)
print(fd.most_common(50))


print("-----All POP words-----")
fd1 = nltk.FreqDist(popWords)
POP_FrequentWords = fd1.most_common(50)
print(fd1.most_common(50))


print("-----All ROCK words-----")
fd2 = nltk.FreqDist(rockWords)
ROCK_FrequentWords = fd2.most_common(50)
print(fd2.most_common(50))

# for wordPop in POP_FrequentWords:
#     for wordRock in ROCK_FrequentWords:
#         if wordPop != "." and wordPop != ","


#fd["string"]
#fd.plot(50)


#
# Example	Description
# fdist = FreqDist(samples)	create a frequency distribution containing the given samples
# fdist[sample] += 1	increment the count for this sample
# fdist['monstrous']	count of the number of times a given sample occurred
# fdist.freq('monstrous')	frequency of a given sample
# fdist.N()	total number of samples
# fdist.most_common(n)	the n most common samples and their frequencies
# for sample in fdist:	iterate over the samples
# fdist.max()	sample with the greatest count
# fdist.tabulate()	tabulate the frequency distribution
# fdist.plot()	graphical plot of the frequency distribution
# fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
# fdist1 |= fdist2	update fdist1 with counts from fdist2
# fdist1 < fdist2	test if samples in fdist1 occur less frequently than in fdist2