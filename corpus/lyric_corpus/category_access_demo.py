from nltk.corpus import CategorizedPlaintextCorpusReader

corpus_root = "./files/"
cat_root = "../categories/"

# Hacky way to specify path for cat.txt. A better way would be to rewrite regex '.*\.txt'...
corpus = CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file=cat_root+'cat.txt', cat_delimiter='+')

# get all categories
cats = corpus.categories()
print(cats)

# access corpus
raw = corpus.raw()

# access words, normal and for a category
words = corpus.words()
words_pop = corpus.words(categories="POP")
words_rock = corpus.words(categories="ROCK")

# access sents, normal and for a category
sents = corpus.sents()
sents_pop = corpus.sents(categories="POP")
sents_rock = corpus.sents(categories="ROCK")

# make lists
word_list = list(words)
sents_list = list(sents)

pop_word_list = list(words_pop)
pop_sents_list = list(sents_pop)

rock_word_list = list(words_rock)
rock_sents_list = list(sents_rock)


'''
# check if categories are complete by counting
print("ALL words: "+ str(len(word_list)))

print("POP words: " +str(len(pop_word_list)))
print("ROCK words: " + str(len(rock_word_list)))
print("CHECK words: "len(pop_word_list)+len(rock_word_list))
'''


'''
# print all categories and filenames in this category
for cat in cats:
    print(cat)
    files = corpus.fileids(categories=cat)
    for filename in files:
        print(filename)
    print("\n")
'''