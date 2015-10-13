import os

count = 0;
for filename in os.listdir("."):
    if filename.startswith("Queen_"):
        os.rename(filename, "Queen_" + str(count) + ".txt")
        count = count + 1