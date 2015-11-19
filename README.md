#Lyrics Predictor

This is the final project for an Artificial Intelligence class, in which we implemented a word predictor for a corpus of Rock and Pop song lyrics. Our algorithm is a weighted combination of an N-gram model with discounting and back-off, and an N-gram for tags. 

Our results and analysis can be found in [the project presentation](https://github.com/Salma-El-Alaoui/lyrics-predictor/blob/master/presentation.pdf) or [the report](https://github.com/Salma-El-Alaoui/lyrics-predictor/blob/master/report.pdf).

## Prerequisites
To run the project use python 3.4

The following dependencies are needed:

- nltk 3
- pandas
- bokeh

## Run the project

### Start from zero

in *corpus/raw/* and *corpus/lyric_corpus/*

1. run **cl_client.py** using a songlist file to crawl lyrics
2. run **corpus_builder.py** to clean the raw data
3. manually remove empty files, non english lyrics, etc.
4. run **category.py** to generate a category file

### Start from corpus

#### Corpus analysis

in *analysis/*

- run **basic_statistics.py** for basic meassurements on corpus
- run **collocation.py** for bigram and trigram collocations in POP and ROCK

#### Word Prediction and further analysis

in *analysis/*

- run **linearCombination.py**
- run **perplexity.py**
- run **predictWord.py**
- run **testSimpleNgram.py**
- run **testSmoothing.py**
- run **tryAlpha.py**

## Models used for NGrams

in *nGram/* the following models and taggers can be found:

- **nGramModel.py**
- **NgramTagModel.py**
- **trainTagger.py**
