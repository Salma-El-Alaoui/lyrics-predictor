import os,glob
import codecs

cat_file_name = "cat.txt"

corpus_dir = "./files/"
categories_dir = "./categories/"

if not os.name == 'posix':
    corpus_dir = ".\\files\\"
    categories_dir = ".\\categories\\"


Artist_POP = ['Justin Timberlake', 'Prince', 'Paul Simon', 'Mariah Carey', 'Britney Spears', 'Simon & Garfunkel',
              'Janet Jackson','Elton John', 'Miley Cyrus', 'Lady Gaga', 'Katy Perry', 'Michael Jackson',
              'Kylie Minogue','Bee Gees', 'George Michael','ABBA','Al Green','Whitney Houston', 'Adele',
              'Andy Williams', 'Maroon 5','Robbie Williams', 'Backstreet Boys', 'Gwen Stefani', 'Madonna',
              'The Beach Boys', 'Barbra Streisand','Christina Aguilera', 'Celine Dion',
              'Prince & The New Power Generation', 'Beyonce', 'Alan Jackson', 'Prince & The Revolution', 'Taylor Swift']

Artist_ROCK = ['The Stone Roses','The Rolling Stones','Radiohead','The Offspring','Red Hot Chili Peppers','Ramones',
               'U2','Linkin Park','Led Zeppelin', 'Iron Maiden', 'Aerosmith', 'Foo Fighters','Pink Floyd', 'ACDC',
               'Green Day', 'Nirvana', 'blink-182','The Clash', 'Queen', '30 Seconds to Mars',
               'Queens of the Stone Age', 'The Doors', 'Metallica', "Guns N' Roses", 'NOFX']


cat_file =  codecs.open(categories_dir+cat_file_name , 'w', encoding='utf-8')

os.chdir(corpus_dir)
for file in glob.glob("*.txt"):

    artist = file.split("_",1)[0]
    artist_cat = artist.replace(" ","")

    if artist in Artist_POP:
        print(file + "+POP+"+artist_cat )
        cat_file.write(file + "+POP+"+artist_cat+"\n")
    else:
        print(file + "+ROCK+"+artist_cat)
        cat_file.write(file + "+ROCK+"+artist_cat+"\n")

cat_file.close()

