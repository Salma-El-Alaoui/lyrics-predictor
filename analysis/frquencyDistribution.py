import nltk
from nltk.corpus import CategorizedPlaintextCorpusReader
from pylab import *

import plotly.plotly as py
import plotly.graph_objs as go

corpus_root = "../corpus/lyric_corpus/files/"
cat_root = "../categories/"

corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')
words = corpus.words()
#frequency distribution

popWords = corpus.words(categories="POP")
rockWords = corpus.words(categories="ROCK")

#print("-----All words-----")
fd = nltk.FreqDist(words)
ALL_FrequentWords = fd.most_common(104)
ALL_FrequentWords_50_100 = []
for i in range(54,104):
	ALL_FrequentWords_50_100.append(ALL_FrequentWords[i])
#print(ALL_FrequentWords)


#print("-----All POP words-----")
fd_POP = nltk.FreqDist(popWords)
POP_FrequentWords = fd_POP.most_common(60)
#print(fd1.most_common(60))


#print("-----All ROCK words-----")
fd_ROCK = nltk.FreqDist(rockWords)
ROCK_FrequentWords = fd_ROCK.most_common(60)
#print(fd2.most_common(60))
#
# mostFrequentWords50 = []
# mostFrequentPopWords50 = []
# mostFrequentRockWords50 = []

# for wordPop in POP_FrequentWords:
#     for wordRock in ROCK_FrequentWords:
#         if wordPop[0] != "." and wordPop[0] != "," :
#             print(wordPop)
#             mostFrequentPopWords50.append(wordPop)
#         if wordRock[0] != "." and wordRock[0] != ",":
#

# for wordPop in POP_FrequentWords:
#     if wordPop[0] != "." and wordPop[0] != "," :
#         print(wordPop)
#         mostFrequentPopWords50.append(wordPop)
MostWordsList = []
POP_Frequency = []
ROCK_Frequency = []
for word in ALL_FrequentWords_50_100:
    if word[0] != "." and word[0] != "," and word[0] != "?" and word[0] != "!" and word[0] != "...":
        #print (word[0])
        MostWordsList.append(word[0])
        POP_Frequency.append(fd_POP[word[0]])
        ROCK_Frequency.append(fd_ROCK[word[0]])



# def plot():
# 	number = []
# 	for i in range(50):
# 		number.append(i)
# 	plot(number,POP_Frequency,'go--',number,ROCK_Frequency,'ro--')
# 	title('Title')
# 	xlabel('X')
# 	ylabel('Y')
# 	grid(True)
# 	show()
#
# plot()
#
trace1 = go.Bar(
    x= MostWordsList,
    y= POP_Frequency,
    name='POP songs'
)
trace2 = go.Bar(
    x=MostWordsList,
    y=ROCK_Frequency,
    name='Rock Songs'
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='songs'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Songs statistics')

# fd["string"]
# fd.plot(50)


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