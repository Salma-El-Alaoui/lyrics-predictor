#reader.fileids(categories=['pos'])
#reader.categories()
#reader.fileids(categories=["POP"])
#CategorizedPlaintextCorpusReader(corpus_root, '.*\.txt', cat_file= 'cat.txt')

import os,glob

Artist_POP = ["ABBA", "Dean Martin"]
Artist_ROCK = ["ACDC", "Frank Sinatra", "Madonna"]
Artist_BLUES = ["Nobody", "Frank Zappa"]

outputFile = open("cat.txt","w")

for file in glob.glob("*.txt"):
    print(file)
    filename = file.split("_",1)
    print(filename[0])
    name = file.split(".",1)
    if filename[0] in Artist_POP:
        outputFile.writelines(file + " " + "POP" + "\n")
    if filename[0] in Artist_ROCK:
        outputFile.writelines(file + " " + "ROCK" + "\n")
    if filename[0] in Artist_BLUES:
        outputFile.writelines(file + " " + "ROCK" + "\n")
    # if filename[0] in Artist_POP:
    #     outputFile.writelines(name[0] + " " + "POP" + "\n")
    # if filename[0] in Artist_ROCK:
    #     outputFile.writelines(name[0] + " " + "ROCK" + "\n")
    # if filename[0] in Artist_BLUES:
    #     outputFile.writelines(name[0] + " " + "ROCK" + "\n")

outputFile.close();
